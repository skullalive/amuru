from abc import ABCMeta, abstractmethod
from enum import Enum
from amurucore.command import Command
from amurucore.exceptions import HandlerException


class CreateHandler(metaclass=ABCMeta):

    @abstractmethod
    def create(self, request:Command):
        raise HandlerException("create method not defined for class {}".format(self.__class__.__name__))
   

class UpdateHandler(metaclass=ABCMeta):

    @abstractmethod
    def update(self, request:Command):
        raise HandlerException("update method not defined for class {}".format(self.__class__.__name__))


class DeleteHandler(metaclass=ABCMeta):

    @abstractmethod
    def delete(self, request:Command):
        raise HandlerException("delete method not defined for class {}".format(self.__class__.__name__))

