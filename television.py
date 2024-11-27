class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self, status: bool = False, muted: bool = False, volume: int = MIN_VOLUME, channel: int = MIN_CHANNEL):
        """
        Sets the initial value of the variables
        :param status: If the TV is off or on
        :param muted: If the TV is muted or not
        :param volume: The current volume of the TV
        :param channel: The current channel of the TV
        """
        self.__status: bool = status
        self.__muted: bool = muted
        self.__volume: int = volume
        self.__channel: int = channel
        self.__muted_volume: int = Television.MIN_VOLUME

    def power(self):
        """
        Turns TV off or on
        :return:
        """
        if self.__status is False:
            self.__status: bool = True
        elif self.__status is True:
            self.__status: bool = False

    def mute(self):
        """
        Mutes TV and saves previous volume in a variable
        :return:
        """
        if self.__status is True:
            if self.__muted is False:
                self.__muted: bool = True
                self.__muted_volume: int = self.__volume
                self.__volume: int = Television.MIN_VOLUME
            elif self.__muted is True:
                self.__muted: bool = False
                self.__volume: int = self.__muted_volume
        else:
            pass

    def channel_up(self):
        """
        Moves the channel value up one, if at the top channel goes to the bottom channel
        :return:
        """
        if self.__status is True:
            if self.__channel != Television.MAX_CHANNEL:
                self.__channel += 1
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel: int = Television.MIN_CHANNEL
        else:
            pass

    def channel_down(self):
        """
        Moves the channel down one, if at bottom channel goes to top channel
        :return:
        """
        if self.__status is True:
            if self.__channel != Television.MIN_CHANNEL:
                self.__channel -= 1
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel: int = Television.MAX_CHANNEL
        else:
            pass

    def volume_up(self):
        """
        Moves the value of the volume up by one, if at max volume it stays the same
        :return:
        """
        if self.__status is True:
            if self.__muted is True:
                Television.mute(self)
            if self.__volume != Television.MAX_VOLUME:
                    self.__volume += 1
            elif self.__volume == Television.MAX_VOLUME:
                    self.__volume: int = Television.MAX_VOLUME
        else:
            pass

    def volume_down(self):
        """
        Moves the value of the volume down one, if at min volume it stays the same
        :return:
        """
        if self.__status is True:
            if self.__muted is True:
                Television.mute(self)
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1
            elif self.__volume == Television.MIN_VOLUME:
                self.__volume: int = Television.MIN_VOLUME
        else:
            pass

    def __str__(self):
        """
        Prints the current status of the power, channel, and volume
        :return:
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
