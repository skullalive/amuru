from typing import Optional
from amurucore.command import Command
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
