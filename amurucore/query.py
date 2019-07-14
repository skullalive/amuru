from amurucore.request import Request


class Query(Request):

    def __init__(self) -> None:
        super().__init__()
    
    @staticmethod
    def is_aQuery() -> bool:
        return True
    
    @staticmethod
    def is_aCommand() -> bool:
        return False