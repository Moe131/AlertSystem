from device import Device
from alert import Alert
from event import Event

class Simulation:
    """ Represents the simulation of our alert system. Contains a length,
    list of devices , and list of events based on the time"""

    def __init__(self, length = 0):
        """Initializes the simulation object with 0 length at the beginning """
        self._length = length
        self._devices = []
        self._events = []

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
        for device in self._devices:
            if device.getID() == ID:
                return device

    def addEvents(self, time:int, senderDeviceID:int, alert: Alert ) -> None:
        """Creates events from a device that has raised an alarm and adds those events
         to the simulation. When an alert is propagated, two events are added,
         one type 'SENT' and one type 'RECEIVED' """
        device = self.getDeviceByID(senderDeviceID)
        for propagation in device.getPropagationList():
            receiverDeviceID = propagation.getReceiverID()
            event1 = Event(time,senderDeviceID,receiverDeviceID, alert, 'SENT')
            self._events.append(event1)
            event2 = Event(time+propagation.getDelay(), senderDeviceID, receiverDeviceID, alert, 'RECEIVED')
            self._events.append(event2)

    def getEvents(self) -> list:
        """Returns a list of events in the simulation"""
        return self._events