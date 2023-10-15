import unittest
from simulation import Simulation

class simulationTest(unittest.TestCase):
    def setUp(self) -> None:
        self._sim = Simulation()


if __name__ == '__main__':
    unittest.main()