import unittest
from amurucore.engine import CommandEngine, QueryEngine
from amurucore.recording import ReceiverRecording
from tests.engine_tests_data import MyTestCommand, MyTestQuery, MyTestQueryWithData, MyTestQueryReceiver, MyTestQueryReceiverWithData, MyTestHandler, MyTestHandlerWithLog


class EngineFixture(unittest.TestCase):
    def setUp(self):
        self._subscriber = ReceiverRecording()
        
    def test_execute(self):
        command = MyTestCommand()
        receiver = MyTestHandler()
        self._subscriber.record(MyTestCommand, lambda: receiver)
        self._command_engine = CommandEngine(self._subscriber)
        self._command_engine.process(command)
        self.assertEqual(receiver._mvalue, "modified value")

    def test_executeWithLogging(self):
        command = MyTestCommand()
        receiver_log = MyTestHandlerWithLog()
        self._subscriber.record(MyTestCommand, lambda: receiver_log)
        self._command_engine = CommandEngine(self._subscriber)
        self._command_engine.process(command)
        self.assertEqual(receiver_log._mvalue, "modified log value")
    
    def test_query(self):
        query = MyTestQuery()
        receiver = MyTestQueryReceiver()
        self._subscriber.record(MyTestQuery, lambda: receiver)
        self._query_engine = QueryEngine(self._subscriber)
        result = self._query_engine.fetch(query)
        self.assertEqual(result, "this is the returned value")

    def test_query_with_data(self):
        query = MyTestQueryWithData()
        receiver = MyTestQueryReceiverWithData()
        self._subscriber.record(MyTestQueryWithData, lambda: receiver)
        self._query_engine = QueryEngine(self._subscriber)
        result = self._query_engine.fetch(query)
        self.assertEqual(result, "myAPropertyValue")
    
    if __name__ == '__main__':
        unittest.main()
