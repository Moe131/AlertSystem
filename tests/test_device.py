import unittest
from device import Device, Propagation

class deviceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._device = Device(1)


    def test_device_ID_is_returned(self):
        self.assertEqual(self._device.getID(), 1)

    def test_propagation_is_added_to_device(self):
        propagation =  Propagation(1,2,500)
        self._device.addPropagation(propagation)
        self.assertEqual(self._device.getPropagationList()[0], propagation)

    def test_propagation_string_returns_correctly(self):
        propagation =  Propagation(1,2,500)
        self.assertEqual(propagation.getPropagationString(), "1 2 500")

    def test_propagation_returns_correct_delay(self):
        propagation =  Propagation(1,2,500)
        self.assertEqual(propagation.getDelay(), 500)

if __name__ == '__main__':
    unittest.main()