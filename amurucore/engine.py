from typing import Optional
from amurucore.command import Command
from amurucore.query import Query
from amurucore.recording import Recording
from amurucore.exceptions import EngineException


class CommandEngine(object):
    def __init__(self, handler_factory: Optional[Recording] = None):
        self.__handler_factory = handler_factory

    def process(self, my_command: Command) -> None:
        if not self.__handler_factory:
            raise EngineException("no command factory found")
        handlers = self.__handler_factory.resolve(my_command)
        for handler in handlers:
            handler_object = handler()
            execute_method = getattr(handler_object, my_command.operation_type.name)
            execute_method(my_command)
            #handler_object.execute(my_command)
    
    

class QueryEngine(object):
    def __init__(self, receiver_factory: Optional[Recording] = None):
        self.__receiver_factory = receiver_factory
    
    def fetch(self, my_query: Query) -> object:
        if not self.__receiver_factory:
            raise EngineException("no query factory found")
        receiver = self.__receiver_factory.resolve(my_query)
        if receiver is None:
            raise EngineException("there must be only one receiver")
        receiver_fecth = receiver()
        return receiver_fecth.execute(my_query)
