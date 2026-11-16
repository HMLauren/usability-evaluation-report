"""Compute report metrics from explicitly mapped, anonymized questionnaire rows."""
import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def number(value, low, high, integer=False):
    if value is None or (isinstance(value, str) and not value.strip()):
        return None, "missing"
    if isinstance(value, bool):
        return None, "invalid"
    try:
        val = Decimal(str(value))
    except (InvalidOperation, ValueError):
        return None, "invalid"
    if not val.is_finite() or not low <= val <= high or (integer and val != val.to_integral_value()):
        return None, "invalid"
    return val, None


def display(value):
    return None if value is None else str(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def mean(values):
    return sum(values) / len(values) if values else None


def metric(value, n, questions, formula, **extra):
    return dict(value=None if value is None else str(value), display=display(value),
                n=n, questions=questions, formula=formula, **extra)


def calculate(data):
    lo, hi = Decimal(str(data["scale_min"])), Decimal(str(data["scale_max"]))
    if not lo.is_finite() or not hi.is_finite() or lo >= hi:
        raise ValueError("Invalid satisfaction scale")
    overall = data.get("overall_question")
    dimensions = data.get("dimension_questions", [])
    nps = data.get("nps_question")
    questions = ([overall] if overall else []) + dimensions + ([nps] if nps else [])
    if len(questions) != len(set(questions)):
        raise ValueError("Overall, dimensions and NPS must use distinct question IDs")
    rows = data["responses"]
    ids = [r["user_id"] for r in rows]
    import re
    if len(ids) != len(set(ids)) or any(not re.fullmatch(r"U[0-9]{2,}", uid) for uid in ids):
        raise ValueError("Unique anonymized U IDs required")
    columns = {q: [] for q in questions}
    excluded = {q: {"missing": 0, "invalid": 0} for q in questions}
    appendix, individual_means = [], []
    for row in rows:
        scores = {}
        for q in questions:
            value, reason = number(row.get(q), Decimal(0) if q == nps else lo,
                                   Decimal(10) if q == nps else hi, q == nps)
            scores[q] = value
            if reason:
                excluded[q][reason] += 1
            else:
                columns[q].append(value)
        vals = [scores[q] for q in dimensions if scores[q] is not None]
        included = bool(dimensions) and len(vals) == len(dimensions)
        personal = mean(vals) if included else None
        if included:
            individual_means.append(personal)
        appendix.append(dict(user_id=row["user_id"],
            scores={q: None if v is None else str(v) for q, v in scores.items()},
            individual_dimension_mean=display(personal), valid_dimension_count=len(vals),
            included=included, exclusion_reason=None if included else "Incomplete or unmapped dimensions"))
    metrics = {}
    if overall:
        metrics["overall_satisfaction"] = metric(mean(columns[overall]), len(columns[overall]),
            [overall], "sum(valid overall scores) / valid overall responses")
    metrics["dimensions"] = {q: metric(mean(columns[q]), len(columns[q]), [q],
        "sum(valid item scores) / valid item responses") for q in dimensions}
    metrics["dimension_composite"] = metric(mean(individual_means), len(individual_means), dimensions,
        "mean(unrounded individual dimension means); complete cases, equal weights")
    if nps:
        vals = columns[nps]
        promoters = sum(v >= 9 for v in vals)
        detractors = sum(v <= 6 for v in vals)
        value = Decimal(promoters - detractors) / len(vals) * 100 if vals else None
        metrics["nps"] = metric(value, len(vals), [nps],
            "(promoters - detractors) / valid NPS responses * 100",
            promoters=promoters, passives=len(vals)-promoters-detractors, detractors=detractors)
    return dict(scale_min=str(lo), scale_max=str(hi), metrics=metrics,
                excluded_by_question=excluded, appendix=appendix)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: calculate_metrics.py input.json output.json")
    from pathlib import Path
    result = calculate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8-sig")))
    Path(sys.argv[2]).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
