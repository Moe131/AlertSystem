import unittest
from simulation import Simulation
from device import Device

class simulationTest(unittest.TestCase):
    def setUp(self) -> None:
        self._sim = Simulation()

    def test_simulation_length_is_changed_successfully(self):
        self._sim.setLength(1000)
        self.assertEqual(self._sim.getLength(), 1000)

    def test_device_is_added_to_simulation(self):
        device = Device(1)
        self._sim.addDevice(device)
        self.assertEqual(self._sim.getDevices()[0],device)

    def test_correct_device_is_returned_when_searching_a_simulation_for_device(self):
        device = Device(2)
        self._sim.addDevice(device)
        self.assertEqual(self._sim.getDeviceByID(2),device)


if __name__ == '__main__':
    unittest.main()