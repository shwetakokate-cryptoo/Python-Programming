"""
Command Design Pattern

This program demonstrates the Command
design pattern by controlling a light
using command objects.
"""

from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract command."""

    @abstractmethod
    def execute(self) -> None:
        """Execute the command."""


class Light:
    """Represents a light."""

    def turn_on(self) -> None:
        print("Light is ON")

    def turn_off(self) -> None:
        print("Light is OFF")


class TurnOnCommand(Command):
    """Command to turn on the light."""

    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.turn_on()


class TurnOffCommand(Command):
    """Command to turn off the light."""

    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.turn_off()


class RemoteControl:
    """Invoker that executes commands."""

    def submit(self, command: Command) -> None:
        command.execute()


def main():

    light = Light()

    turn_on = TurnOnCommand(light)
    turn_off = TurnOffCommand(light)

    remote = RemoteControl()

    remote.submit(turn_on)
    remote.submit(turn_off)


if __name__ == "__main__":
    main()
