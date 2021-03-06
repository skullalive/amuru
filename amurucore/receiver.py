from abc import ABCMeta, abstractmethod
from amurucore.request import Request

class Receiver(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, request:Request) -> object:
        pass

