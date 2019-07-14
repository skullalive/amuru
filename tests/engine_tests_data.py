import logging
from amurucore.query import Query
from amurucore.command import Command
from amurucore.receiver import Receiver, QueryReceiver
from amurucore.request import Request
from amurucore.receiver_log import receiver_log, OutputType


class MyTestHandler(Receiver):
    def __init__(self):
        self._mvalue = "base value"

    def execute(self, request: Request):
        self._mvalue = "modified value"


class MyTestHandlerWithLog(Receiver):
    def __init__(self):
        self._mvalue = "base log value"

    @receiver_log(logging.DEBUG, OutputType.file_output)
    def execute(self, request: Request):
        self._mvalue = "modified log value"


class MyTestQueryReceiver(QueryReceiver):
    def __init__(self):
        pass

    def execute(self, request: Request):
        return "this is the returned value"


class MyTestQuery(Query):
    def __init__(self):
        super().__init__()


class MyTestCommand(Command):
    def __init__(self):
        super().__init__()
