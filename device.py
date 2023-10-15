class Propagation:
    """Represents a propagation and contains
     senderDeviceID, receiverDeviceID, and delay"""
    def __init__(self, senderDeviceID:int , receiverDeviceID:int, delay:int ):
        """Initializes a propagation with the three attributes"""
        self.senderDeviceID = senderDeviceID
        self.receiverDeviceID = receiverDeviceID
        self._delay = delay

    def getPropagationString(self) -> str:
        """Returns the propagation attributes in a string to help
         identify propagation with test cases"""
        return f'{self.senderDeviceID} {self.receiverDeviceID} {self._delay}'

class Device:
    """Represents a device in our simulation that has unique ID,
     a propagation list and a list of cancelled alerts"""

    def __init__(self, ID: int):
        """Initializes Device object with a unique ID attribute"""
        self._ID = ID
        self._propagationList = []

    def getID(self) -> int:
        """Returns the ID of the device"""
        return self._ID

    def addPropagation(self, propagation:Propagation) -> None:
        """ Adds a propagation to the device"""
        self._propagationList.append(propagation)

    def getPropagationList(self) -> list:
        """Returns the list of device propagations"""
        return self._propagationList