import unittest
from device import Device

class deviceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._device = Device(1)


    def test_device_ID_is_returned(self):
        self.assertEqual(self._device.getID(), 1)

if __name__ == '__main__':
    unittest.main()