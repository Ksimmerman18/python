class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status = False, muted = False, volume = MIN_VOLUME, channel = MIN_CHANNEL):
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel
        self.__muted_volume = Television.MIN_VOLUME

    def power(self):
        if self.__status is False:
            self.__status = True
        elif self.__status is True:
            self.__status = False

    def mute(self):
        if self.__status is True:
            if self.__muted is False:
                self.__muted = True
                self.__muted_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            elif self.__muted is True:
                self.__muted = False
                self.__volume = self.__muted_volume
        else:
            pass

    def channel_up(self):
        if self.__status is True:
            if self.__channel != Television.MAX_CHANNEL:
                self.__channel += 1
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
        else:
            pass

    def channel_down(self):
        if self.__status is True:
            if self.__channel != Television.MIN_CHANNEL:
                self.__channel -= 1
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
        else:
            pass

    def volume_up(self):
        if self.__status is True:
            if self.__muted is True:
                Television.mute(self)
            if self.__volume != Television.MAX_VOLUME:
                    self.__volume += 1
            elif self.__volume == Television.MAX_VOLUME:
                    self.__volume = Television.MAX_VOLUME
        else:
            pass

    def volume_down(self):
        if self.__status is True:
            if self.__muted is True:
                Television.mute(self)
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1
            elif self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
        else:
            pass

    def __str__(self):
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"