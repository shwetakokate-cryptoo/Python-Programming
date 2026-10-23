"""
Dynamic Programming - Fibonacci

This program demonstrates the Fibonacci sequence
using recursion and dynamic programming (memoization).
"""


class Fibonacci:
    """Implements Fibonacci algorithms."""

    @staticmethod
    def recursive(number: int) -> int:
        """Return the nth Fibonacci number using recursion."""

        if number <= 1:
            return number

        return (
            Fibonacci.recursive(number - 1)
            + Fibonacci.recursive(number - 2)
        )

    @staticmethod
    def memoization(
        number: int,
        memo: dict[int, int] | None = None
    ) -> int:
        """Return the nth Fibonacci number using memoization."""

        if memo is None:
            memo = {}

        if number in memo:
            return memo[number]

        if number <= 1:
            return number

        memo[number] = (
            Fibonacci.memoization(number - 1, memo)
            + Fibonacci.memoization(number - 2, memo)
        )

        return memo[number]


def main():

    number = 10

    print(f"Recursive Fibonacci({number}):")
    print(Fibonacci.recursive(number))

    print()

    print(f"Dynamic Programming Fibonacci({number}):")
    print(Fibonacci.memoization(number))


if __name__ == "__main__":
    main()
