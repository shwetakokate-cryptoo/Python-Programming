"""
Merge Sort Algorithm

This program demonstrates the Merge Sort
algorithm using the Divide and Conquer approach.
"""


class MergeSort:
    """Implements the Merge Sort algorithm."""

    @staticmethod
    def sort(numbers: list[int]) -> list[int]:
        """Return a sorted list using Merge Sort."""

        if len(numbers) <= 1:
            return numbers

        middle = len(numbers) // 2

        left = MergeSort.sort(numbers[:middle])
        right = MergeSort.sort(numbers[middle:])

        return MergeSort._merge(left, right)

    @staticmethod
    def _merge(left: list[int], right: list[int]) -> list[int]:
        """Merge two sorted lists into one sorted list."""

        merged = []

        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):

            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged


def main():

    numbers = [38, 27, 43, 3, 9, 82, 10]

    print("Original List:")
    print(numbers)

    sorted_numbers = MergeSort.sort(numbers)

    print("\nSorted List:")
    print(sorted_numbers)


if __name__ == "__main__":
    main()
