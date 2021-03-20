from design_patterns.command_pattern.command_interface import AbstractCommand
from design_patterns.command_pattern.order_command_interface import AbstractOrderCommand


class Action1(AbstractCommand,AbstractOrderCommand):
    name="action_1"
    description="example action. 1"

    def __init__(self, args):
        self.first_argument = args[1]

    def execute(self):
        print("action 1:"+self.first_argument)

