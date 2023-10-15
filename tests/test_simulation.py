import unittest
from simulation import Simulation

class simulationTest(unittest.TestCase):
    def setUp(self) -> None:
        self._sim = Simulation()

    def test_simulation_length_is_changed_successfully(self):
        self._sim.setLength(1000)
        self.assertEqual(self._sim.getLength(), 1000)


if __name__ == '__main__':
    unittest.main()