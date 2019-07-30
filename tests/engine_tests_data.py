import logging
from amurucore.query import Query
from amurucore.command import Command
from amurucore.receiver import Receiver
from amurucore.handler import UpdateHandler, CreateHandler
from amurucore.request import Request
from amurucore.receiver_log import receiver_log, OutputType


class MyTestHandler(UpdateHandler):
    def __init__(self):
        self._mvalue = "base value"
            
    def update(self, request:Command):
        self._mvalue = "modified value"


class MyTestHandlerWithLog(UpdateHandler):
    def __init__(self):
        self._mvalue = "base log value"

    @receiver_log(logging.DEBUG, OutputType.file_output)
    def update(self, request: Request):
        self._mvalue = "modified log value"


class MyTestQueryReceiver(Receiver):
    def __init__(self):
        pass

    def execute(self, request: Request):
        return "this is the returned value"


class MyTestQueryReceiverWithData(Receiver):
    def __init__(self):
        pass

    def execute(self, request: Request):
        return request.propA

class MyTestQuery(Query):
    def __init__(self):
        super().__init__()


class MyTestQueryWithData(Query):
    def __init__(self):
        self.__propA = "myAPropertyValue"
        super().__init__()
    
    @property
    def propA(self):
        return self.__propA

class MyTestCommand(Command):
    def __init__(self):
        super().__init__()
