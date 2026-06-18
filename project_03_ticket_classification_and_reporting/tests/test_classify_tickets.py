import unittest
from project_03_ticket_classification_and_reporting.src.classify_tickets import classify_description


class ClassifyTicketsTests(unittest.TestCase):
    def test_unlock_precedence_over_payment(self):
        category, _ = classify_description("Unlock needed before payment can process")
        self.assertEqual(category, "card_unlock")

    def test_compliance_review_detected(self):
        category, _ = classify_description("High risk compliance exception")
        self.assertEqual(category, "compliance_review")

    def test_other_when_no_match(self):
        category, _ = classify_description("General documentation request")
        self.assertEqual(category, "other")


if __name__ == "__main__":
    unittest.main()
