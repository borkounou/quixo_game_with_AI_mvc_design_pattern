from abc import ABCMeta, abstractmethod

class IPlayer(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,name):
        """Implements de name and player number"""

    @abstractmethod
    def playing(self, *args, **kwargs):
        """Implements """


