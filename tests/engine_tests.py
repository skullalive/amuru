from unittest import TestCase
from Core.engine import CommandEngine
from Core.recording import ReceiverRecording
from tests.engine_tests_data import MyTestCommand, MyTestHandler, MyTestHandlerWithLog


class EngineFixture(TestCase):
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
