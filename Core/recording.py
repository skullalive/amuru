from typing import Callable
from Core.receiver import Request
from Core.command import Command

class ReceiverRecording(object):
    def __init__(self) -> None:
        self._recording = {}

    
    def record(self, request:Command, implementation:Callable[[], Request]) -> None:
        key = request.__name__
        self._recording[key].append(implementation)
    
    def resolve(self, request_object:Command) -> Callable[[], Request]:
        key = request_object.__class__.__name__
        if key not in self._recording.keys():
            raise Exception("no receiver found for this command")
        
        return self._recording[key]

    
    

    
    
        