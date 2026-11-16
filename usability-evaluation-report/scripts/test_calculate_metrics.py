import unittest
from calculate_metrics import calculate

class MetricsTests(unittest.TestCase):
    def run_data(self, rows):
        return calculate(dict(scale_min=1, scale_max=10, overall_question="o",
            dimension_questions=["a", "b"], nps_question="n", responses=rows))

    def test_known_results_and_separate_questions(self):
        rows = [dict(user_id=f"U{i:02}",o=o,a=a,b=b,n=n) for i,(o,a,b,n) in enumerate(
            [(8,6,10,10),(9,8,10,9),(9,10,10,8),(None,None,9,6)],1)]
        out = self.run_data(rows)
        self.assertEqual(out["metrics"]["nps"]["display"], "25.00")
        self.assertEqual(out["metrics"]["overall_satisfaction"]["display"], "8.67")
        self.assertEqual(out["metrics"]["dimensions"]["b"]["n"], 4)
        self.assertEqual(out["metrics"]["dimension_composite"]["display"], "9.00")
        self.assertEqual(out["metrics"]["dimension_composite"]["n"], 3)
        self.assertFalse(out["appendix"][3]["included"])

    def test_zero_missing_invalid_and_empty(self):
        out = self.run_data([dict(user_id="U01",n=0,o=True),dict(user_id="U02",n=None),
                             dict(user_id="U03",n=10),dict(user_id="U04",n=11)])
        self.assertEqual(out["metrics"]["nps"]["display"], "0.00")
        self.assertEqual(out["metrics"]["nps"]["n"], 2)
        self.assertEqual(out["excluded_by_question"]["n"],dict(missing=1,invalid=1))
        self.assertIsNone(out["metrics"]["overall_satisfaction"]["value"])
        self.assertIsNone(self.run_data([])["metrics"]["nps"]["value"])

    def test_reject_duplicate_identity(self):
        with self.assertRaises(ValueError):
            self.run_data([dict(user_id="U01"),dict(user_id="U01")])

    def test_extremes_and_rounding(self):
        for score, expected in [(10,"100.00"),(0,"-100.00"),(7,"0.00")]:
            self.assertEqual(self.run_data([dict(user_id="U01",n=score,o="8.005")])["metrics"]["nps"]["display"],expected)
        self.assertEqual(self.run_data([dict(user_id="U01",o="8.005")])["metrics"]["overall_satisfaction"]["display"],"8.01")

if __name__ == "__main__":
    unittest.main()
