"""
Quick Sort Algorithm

This program demonstrates the Quick Sort
algorithm using the Divide and Conquer approach.
"""


class QuickSort:
    """Implements the Quick Sort algorithm."""

    @staticmethod
    def sort(numbers: list[int]) -> None:
        """Sort the list in ascending order."""

        QuickSort._quick_sort(numbers, 0, len(numbers) - 1)

    @staticmethod
    def _quick_sort(numbers: list[int], low: int, high: int) -> None:

        if low < high:

            pivot_index = QuickSort._partition(numbers, low, high)

            QuickSort._quick_sort(numbers, low, pivot_index - 1)
            QuickSort._quick_sort(numbers, pivot_index + 1, high)

    @staticmethod
    def _partition(numbers: list[int], low: int, high: int) -> int:

        pivot = numbers[high]

        index = low - 1

        for current in range(low, high):

            if numbers[current] <= pivot:
                index += 1
                numbers[index], numbers[current] = (
                    numbers[current],
                    numbers[index],
                )

        numbers[index + 1], numbers[high] = (
            numbers[high],
            numbers[index + 1],
        )

        return index + 1


def main():

    numbers = [38, 27, 43, 3, 9, 82, 10]

    print("Original List:")
    print(numbers)

    QuickSort.sort(numbers)

    print("\nSorted List:")
    print(numbers)


if __name__ == "__main__":
    main()
