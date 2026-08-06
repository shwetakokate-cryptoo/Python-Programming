"""
Decorator Design Pattern

This program demonstrates the Decorator
design pattern by adding extra features
to a coffee order.
"""

from abc import ABC, abstractmethod


class Coffee(ABC):
    """Abstract coffee component."""

    @abstractmethod
    def cost(self) -> float:
        """Return the total cost."""

    @abstractmethod
    def description(self) -> str:
        """Return the coffee description."""


class SimpleCoffee(Coffee):
    """Basic coffee."""

    def cost(self) -> float:
        return 100.0

    def description(self) -> str:
        return "Simple Coffee"


class CoffeeDecorator(Coffee):
    """Base decorator."""

    def __init__(self, coffee: Coffee):
        self.coffee = coffee

    def cost(self) -> float:
        return self.coffee.cost()

    def description(self) -> str:
        return self.coffee.description()


class MilkDecorator(CoffeeDecorator):
    """Adds milk to the coffee."""

    def cost(self) -> float:
        return self.coffee.cost() + 20.0

    def description(self) -> str:
        return self.coffee.description() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    """Adds sugar to the coffee."""

    def cost(self) -> float:
        return self.coffee.cost() + 10.0

    def description(self) -> str:
        return self.coffee.description() + ", Sugar"


def main():

    coffee = SimpleCoffee()

    coffee = MilkDecorator(coffee)
    coffee = SugarDecorator(coffee)

    print("Order:", coffee.description())
    print(f"Total Cost: ₹{coffee.cost():.2f}")


if __name__ == "__main__":
    main()
