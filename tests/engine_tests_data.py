from Core.command import Command
from Core.receiver import Receiver


class MyTestHandler(Receiver):
    def __init__(self):
        self._mvalue = "base value"
    
    def execute(self, request):
        self._mvalue = "modified value"
        


class MyTestCommand(Command):
    def __init__(self):
        super().__init__()
    
    
