class Simulation:
    """ Represents the simulation of our alert system. Contains a length,
    list of devices , and list of events based on the time"""

    def __init__(self, length = 0):
        """Initializes the simulation object with 0 length at the beginning """
        self._length = length

    def setLength(self, length:int) -> None :
        """Sets the length of the simulation to new value"""
        self._length = length

    def getLength(self) -> int:
        """Returns the length of the simulation"""
        return self._length