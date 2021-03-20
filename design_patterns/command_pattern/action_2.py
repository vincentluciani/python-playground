from design_patterns.command_pattern.command_interface import AbstractCommand
from design_patterns.command_pattern.order_command_interface import AbstractOrderCommand


class Action2(AbstractCommand,AbstractOrderCommand):
    name="action_2"
    description="example action. 2"

    def __init__(self, args):
        self.first_argument = args[1]

    def execute(self):
        print("action 2:"+self.first_argument)

