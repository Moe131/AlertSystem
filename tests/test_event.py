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


if __name__ == '__main__':
    unittest.main()