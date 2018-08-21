__all__ = ["DeviceOrientation"]


class DeviceOrientation(object):
    def __init__(self, chrome):
        """
        Construct a new DeviceOrientation object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def clearDeviceOrientationOverride(self):
        """
        Clears the overridden Device Orientation.
        """
        wres = self.chrome.send('DeviceOrientation.clearDeviceOrientationOverride')
        return wres.get()

    def setDeviceOrientationOverride(self, alpha, beta, gamma):
        """
        Overrides the Device Orientation.

        :param alpha: Mock alpha
        :type alpha: float
        :param beta: Mock beta
        :type beta: float
        :param gamma: Mock gamma
        :type gamma: float
        """
        msg_dict = dict()
        if alpha is not None:
            msg_dict['alpha'] = alpha
        if beta is not None:
            msg_dict['beta'] = beta
        if gamma is not None:
            msg_dict['gamma'] = gamma
        wres = self.chrome.send('DeviceOrientation.setDeviceOrientationOverride', msg_dict)
        return wres.get()

