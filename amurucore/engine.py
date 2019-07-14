from typing import Optional
from amurucore.command import Command
from amurucore.query import Query
from amurucore.recording import ReceiverRecording
from amurucore.exceptions import EngineException


class CommandEngine(object):
    def __init__(self, receiver_factory: Optional[ReceiverRecording] = None):
        self._receiver_factory = receiver_factory

    def process(self, my_command: Command) -> None:
        if not self._receiver_factory:
            raise EngineException("no factory found")
        receivers = self._receiver_factory.resolve(my_command)
        for receiver in receivers:
            receiver_object = receiver()
            receiver_object.execute(my_command)
    
    

class QueryEngine(object):
    def __init__(self, receiver_factory: Optional[ReceiverRecording] = None):
        self._receiver_factory = receiver_factory
    
    def fetch(self, my_query: Query) -> object:
        if not self._receiver_factory:
            raise EngineException("no query fctory found")
        receiver = self._receiver_factory.resolve(my_query)
        if receiver is None:
            raise EngineException("there must be only one receiver")
        receiver_fecth = receiver()
        return receiver_fecth.execute(my_query)
