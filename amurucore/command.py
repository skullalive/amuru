from amurucore.request import Request
from enum import Enum

class CommandOperator(Enum):
    create=1
    update=2
    delete=3

class Command(Request):

    def __init__(self) -> None:
        self.operation_type = None
        super().__init__()
    
    @staticmethod
    def is_aCommand() -> bool:
        return True
    
    @staticmethod
    def is_aQuery() -> bool:
        return False