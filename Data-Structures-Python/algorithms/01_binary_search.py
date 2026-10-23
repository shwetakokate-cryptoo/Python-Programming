"""
Binary Search Algorithm

This program demonstrates the Binary Search
algorithm on a sorted list.
"""


class BinarySearch:
    """Implements the Binary Search algorithm."""

    @staticmethod
    def search(numbers: list[int], target: int) -> int:
        """Return the index of the target if found, otherwise -1."""

        left = 0
        right = len(numbers) - 1

        while left <= right:

            middle = (left + right) // 2

            if numbers[middle] == target:
                return middle

            if numbers[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1


def main():

    numbers = [10, 20, 30, 40, 50, 60, 70]
    target = 50

    index = BinarySearch.search(numbers, target)

    if index != -1:
        print(f"{target} found at index {index}.")
    else:
        print(f"{target} not found.")


if __name__ == "__main__":
    main()
