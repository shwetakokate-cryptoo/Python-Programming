"""
Adapter Design Pattern

This program demonstrates the Adapter
design pattern by adapting a legacy
printer to a modern printing interface.
"""

from abc import ABC, abstractmethod


class Printer(ABC):
    """Abstract printer interface."""

    @abstractmethod
    def print_document(self, document: str) -> None:
        """Print a document."""


class LegacyPrinter:
    """Represents an old printer."""

    def print_text(self, text: str) -> None:
        print(f"Legacy Printer: {text}")


class PrinterAdapter(Printer):
    """Adapts LegacyPrinter to the Printer interface."""

    def __init__(self, printer: LegacyPrinter):
        self.printer = printer

    def print_document(self, document: str) -> None:
        self.printer.print_text(document)


def main():

    legacy_printer = LegacyPrinter()

    adapter = PrinterAdapter(legacy_printer)

    adapter.print_document("Design Patterns in Python")


if __name__ == "__main__":
    main()
