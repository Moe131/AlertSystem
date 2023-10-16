import unittest
from alert import Alert

class alertTest(unittest.TestCase):
    def setUp(self) -> None:
        self._alert = Alert('Trouble')

    def test_alert_returns_correct_description(self):
        self.assertEqual(self._alert.getDescription(), "Trouble")

    def test_alert_is_cancellation_type(self):
        self._alert = Alert('Problem', True)
        self.assertTrue(self._alert.isCancel())

if __name__ == '__main__':
    unittest.main()