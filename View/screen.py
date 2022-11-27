from abc import ABCMeta, abstractmethod
class IScreen(metaclass=ABCMeta):

    @abstractmethod
    def draw_screen(self,*args, **kwargs):
        """Implements different screens to display"""