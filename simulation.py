from device import Device

class Simulation:
    """ Represents the simulation of our alert system. Contains a length,
    list of devices , and list of events based on the time"""

    def __init__(self, length = 0):
        """Initializes the simulation object with 0 length at the beginning """
        self._length = length
        self._devices = []

    def setLength(self, length:int) -> None :
        """Sets the length of the simulation to new value"""
        self._length = length

    def getLength(self) -> int:
        """Returns the length of the simulation"""
        return self._length

    def addDevice(self, device: Device):
        """Adds a device to simulation's devices list"""
        self._devices.append(device)

    def getDevices(self) -> list:
        """Returns a list of devices in the simulation"""
        return self._devices

    def getDeviceByID(self,ID:int)-> Device:
        """Searches for a device in simulation base on the ID and returns it """
        for device in self.getDevices():
            if device.getID() == ID:
                return device
