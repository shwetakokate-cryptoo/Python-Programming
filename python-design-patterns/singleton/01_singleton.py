"""
Singleton Design Pattern

This program demonstrates the Singleton design pattern,
which ensures that only one instance of a class exists.
"""


class Singleton:
    """Represents a Singleton class."""

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        self.application_name = "Python Design Patterns"


def main():

    first = Singleton()
    second = Singleton()

    print("First Instance ID :", id(first))
    print("Second Instance ID:", id(second))

    print()

    print("Same Instance:", first is second)

    print()

    print("Application Name:", first.application_name)


if __name__ == "__main__":
    main()
