from design_patterns.command_pattern.command_interface import AbstractCommand
from design_patterns.command_pattern.order_command_interface import AbstractOrderCommand


class NoAction(AbstractCommand):

    def __init__(self, args):
        self._command = args[0]
        self.first_argument = args[1]
        pass

    def execute(self):
        print("No command named:"+self._command)

