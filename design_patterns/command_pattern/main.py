import sys

from design_patterns.command_pattern.action_1 import Action1
from design_patterns.command_pattern.action_2 import Action2
from design_patterns.command_pattern.no_action import NoAction


def get_commands():
    commands = (Action1,Action2)
    return dict([command.name,command] for command in commands)

def print_usage(commands):
    print("Command Commandname [arguments]")
    for command in commands.values():
        print(command.description)

def parse_command(commands, args):
    command = commands.setdefault(args[0], NoAction) #find args[0] in command, assign NoAction if not found
    return command(args)

commands = get_commands()
if len(sys.argv) < 2:
    print_usage(commands)
    exit()


command = parse_command(commands, sys.argv[1:])
command.execute()


