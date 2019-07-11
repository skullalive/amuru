from typing import Callable, List
from Core.receiver import Receiver
from Core.request import Request
from Core.command import Command
from Core.exceptions import RecordingException


class ReceiverRecording(object):
    def __init__(self) -> None:
        self._recording = {}

    def record(self, request:Command, implementation:Callable[[], Receiver]) -> None:
        key = request.__name__
        if request.is_aCommand() and key in self._recording.keys():
            self._recording[key].append(implementation)
        else:
            self._recording[key] = [implementation]

    def resolve(self, request_object: Command) -> List[Callable[[], Receiver]]:
        key = request_object.__class__.__name__
        if key not in self._recording.keys():
            raise RecordingException("no receiver found for this command")

        return self._recording[key]