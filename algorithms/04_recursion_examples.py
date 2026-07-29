"""
Recursion Examples

This program demonstrates common recursive
algorithms including factorial, Fibonacci,
sum of first n numbers, and string reversal.
"""


class RecursionExamples:
    """Collection of recursive algorithms."""

    @staticmethod
    def factorial(number: int) -> int:
        """Return the factorial of a number."""

        if number <= 1:
            return 1

        return number * RecursionExamples.factorial(number - 1)

    @staticmethod
    def fibonacci(number: int) -> int:
        """Return the nth Fibonacci number."""

        if number <= 1:
            return number

        return (
            RecursionExamples.fibonacci(number - 1)
            + RecursionExamples.fibonacci(number - 2)
        )

    @staticmethod
    def sum_of_numbers(number: int) -> int:
        """Return the sum of the first n natural numbers."""

        if number == 1:
            return 1

        return number + RecursionExamples.sum_of_numbers(number - 1)

    @staticmethod
    def reverse_string(text: str) -> str:
        """Return the reversed string."""

        if len(text) <= 1:
            return text

        return (
            RecursionExamples.reverse_string(text[1:])
            + text[0]
        )


def main():

    print("Factorial of 5:")
    print(RecursionExamples.factorial(5))

    print("\n10th Fibonacci Number:")
    print(RecursionExamples.fibonacci(10))

    print("\nSum of First 10 Numbers:")
    print(RecursionExamples.sum_of_numbers(10))

    print("\nReverse of 'Python':")
    print(RecursionExamples.reverse_string("Python"))


if __name__ == "__main__":
    main()
