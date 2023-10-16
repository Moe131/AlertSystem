class Alert:
    """ Class Alert represents an alert request that devices can
     raise, and it can be a CANCEL type or not
     """
    def __init__(self, description:str, isCancel= False):
        """Initializes Alert object"""
        self._description = description
        self._isCancel = isCancel

    def getDescription(self):
        """Returns the description of the alert"""
        return self._description

    def isCancel(self):
        """Returns true if the alert is a cancellation type of alert"""
        return self._isCancel