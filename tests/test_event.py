import unittest
from event import Event
from alert import Alert

class eventTest(unittest.TestCase):
    def setUp(self) -> None:
        self._alert = Alert("Trouble")
        self._event = Event(0,1,2, self._alert,'SENT')

    def test_event_time_is_returned(self):
        self.assertEqual(self._event.getTime(),0)

    def test_event_alert_is_returned(self):
        self.assertEqual(self._event.getAlert(),self._alert)

    def test_event_type_is_returned(self):
        self.assertEqual(self._event.getType(), 'SENT')

    def test_event_toString_method_returns_correct_format(self):
        event = Event(0, 1, 2, Alert("Trouble"), 'SENT')
        self.assertEqual(event.toString(), "@0: #1 SENT ALERT TO #2: Trouble")
        event = Event(0, 1, 2, Alert("Trouble"), 'RECEIVED')
        self.assertEqual(event.toString(), "@0: #2 RECEIVED ALERT FROM #1: Trouble")
        event = Event(0, 1, 2, Alert("Trouble", True), 'SENT')
        self.assertEqual(event.toString(), "@0: #1 SENT CANCELLATION TO #2: Trouble")
        event = Event(0, 1, 2, Alert("Trouble", True), 'RECEIVED')
        self.assertEqual(event.toString(), "@0: #2 RECEIVED CANCELLATION FROM #1: Trouble")

if __name__ == '__main__':
    unittest.main()