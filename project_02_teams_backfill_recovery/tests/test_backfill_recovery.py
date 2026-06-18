import unittest
from project_02_teams_backfill_recovery.src.backfill_recovery import clean_html, recover_tracker_rows


class BackfillRecoveryTests(unittest.TestCase):
    def test_clean_html_decodes_entities_and_removes_tags(self):
        self.assertEqual(clean_html("<p>Hello &amp; welcome</p>"), "Hello & welcome")

    def test_recover_tracker_rows_excludes_thread_replies(self):
        tracker_rows = [{
            "tracker_id": "trk-1",
            "message_id": "m-1",
            "logged_at": "",
            "sender_name": "",
            "manager_email": "",
            "content": "",
            "recovery_status": "Needs Recovery",
        }]
        messages = [{
            "message_id": "m-1",
            "sent_at": "2026-03-01T09:00:00",
            "sender_name": "Agent One",
            "manager_email": "manager@example.com",
            "body_html": "<p>Recovered</p>",
            "is_reply": "true",
        }]
        recovered = recover_tracker_rows(tracker_rows, messages)
        self.assertEqual(recovered[0]["recovery_status"], "No matching source message")


if __name__ == "__main__":
    unittest.main()
