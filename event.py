from alert import Alert
class Event:
    """Represents an event in our simulation that has
     senderDeviceID, receiverDeviceID, time, Alert, and  'SENT' or 'RECEIVED' type"""
    def __init__(self, time:int, senderDeviceID:int, receiverDeviceID:int, alert:Alert, type:str):
        """Initializes an event with all the parameters"""
        self._time = time
        self._senderDeviceID = senderDeviceID
        self._receiverDeviceID =  receiverDeviceID
        self._alert = alert
        self._type = type

    def getTime(self) -> int :
        """Returns the time of the event"""
        return self._time

    def getAlert(self) -> Alert :
        """Returns the alert of the event"""
        return self._alert

    def getType(self) -> str:
        """Returns the type of the event"""
        return self._type

    def getSenderID(self) -> int:
        """Returns the ID of sender device"""
        return self._senderDeviceID

    def getReceiverID(self) -> int:
        """Returns the ID of receiver device"""
        return self._receiverDeviceID

    def toString(self) -> str:
        """Converts the event to a string format and returns it"""
        if self._type == 'SENT' and not self._alert.isCancel():
            return (f'@{self._time}: #{self._senderDeviceID} SENT'
                    f' ALERT TO #{self._receiverDeviceID}: {self._alert.getDescription()}')

        elif self._type == 'SENT' and self._alert.isCancel():
            return (f'@{self._time}: #{self._senderDeviceID} SENT'
                    f' CANCELLATION TO #{self._receiverDeviceID}: {self._alert.getDescription()}')

        elif self._type == 'RECEIVED' and self._alert.isCancel():
            return (f'@{self._time}: #{self._receiverDeviceID} RECEIVED'
                    f' CANCELLATION FROM #{self._senderDeviceID}: {self._alert.getDescription()}')

        elif self._type == 'RECEIVED' and not self._alert.isCancel():
            return (f'@{self._time}: #{self._receiverDeviceID} RECEIVED'
                    f' ALERT FROM #{self._senderDeviceID}: {self._alert.getDescription()}')