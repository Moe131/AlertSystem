class Device:
    """Represents a device in our simulation that has unique ID,
     a propagation list and a list of cancelled alerts"""

    def __init__(self, ID: int):
        """Initializes Device object with a unique ID attribute"""
        self._ID = ID

    def getID(self) -> int:
        """Returns the ID of the device"""
        return self._ID
