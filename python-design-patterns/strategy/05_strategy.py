"""
Strategy Design Pattern

This program demonstrates the Strategy
design pattern by allowing different
payment methods to be selected at runtime.
"""

from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    """Abstract payment strategy."""

    @abstractmethod
    def pay(self, amount: float) -> None:
        """Process the payment."""


class CreditCardPayment(PaymentStrategy):
    """Payment using a credit card."""

    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount:.2f} using Credit Card.")


class UpiPayment(PaymentStrategy):
    """Payment using UPI."""

    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount:.2f} using UPI.")


class PayPalPayment(PaymentStrategy):
    """Payment using PayPal."""

    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount:.2f} using PayPal.")


class PaymentProcessor:
    """Uses a selected payment strategy."""

    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        """Change the payment strategy."""

        self.strategy = strategy

    def checkout(self, amount: float) -> None:
        """Process the payment."""

        self.strategy.pay(amount)


def main():

    processor = PaymentProcessor(CreditCardPayment())

    processor.checkout(1500)

    processor.set_strategy(UpiPayment())
    processor.checkout(750)

    processor.set_strategy(PayPalPayment())
    processor.checkout(2200)


if __name__ == "__main__":
    main()
