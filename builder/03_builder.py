"""
Builder Design Pattern

This program demonstrates the Builder
design pattern by constructing a computer
object step by step.
"""


class Computer:
    """Represents a computer."""

    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.graphics_card = None

    def display(self) -> None:
        """Display the computer specifications."""

        print("Computer Configuration")
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print(f"Graphics Card: {self.graphics_card}")


class ComputerBuilder:
    """Builds a computer object."""

    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu: str):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram: str):
        self.computer.ram = ram
        return self

    def set_storage(self, storage: str):
        self.computer.storage = storage
        return self

    def set_graphics_card(self, graphics_card: str):
        self.computer.graphics_card = graphics_card
        return self

    def build(self) -> Computer:
        return self.computer


def main():

    computer = (
        ComputerBuilder()
        .set_cpu("Intel Core i7")
        .set_ram("16 GB")
        .set_storage("512 GB SSD")
        .set_graphics_card("NVIDIA RTX 4060")
        .build()
    )

    computer.display()


if __name__ == "__main__":
    main()
