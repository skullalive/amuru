from typing import Callable, List
from amurucore.receiver import Receiver
from amurucore.request import Request
from amurucore.command import Command
from amurucore.exceptions import RecordingException


class Recording(object):
    def __init__(self) -> None:
        self.__recording = {}

    def record(self, request:Request, implementation:Callable[[], Receiver]) -> None:
        key = request.__name__
        if request.is_aCommand():
            if key in self.__recording.keys():
                self.__recording[key].append(implementation)
            else:
                self.__recording[key] = [implementation]
        else:
            if key in self.__recording.keys():
                raise RecordingException("Query already exists")
            self.__recording[key] = implementation


    def resolve(self, request_object: Request) -> List[Callable[[], Receiver]]:
        key = request_object.__class__.__name__
        if key not in self.__recording.keys():
            raise RecordingException("no receiver found for request {}".format(key))

        return self.__recording[key]
    
    def clear(self):
        self.__recording.clear()
