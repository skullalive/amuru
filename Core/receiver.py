from abc import ABCMeta, abstractmethod
from Core.request import Request

class Receiver(metaclass=ABCMeta):

    @abstractmethod
    def Execute(self, request:Request) -> Request:
        pass
