"""
Two Sum Algorithm

This program finds the indices of two numbers
whose sum equals a given target using a hash map.
"""


class TwoSum:
    """Implements the Two Sum algorithm."""

    @staticmethod
    def find(numbers: list[int], target: int) -> list[int]:

        lookup: dict[int, int] = {}

        for index, number in enumerate(numbers):

            complement = target - number

            if complement in lookup:
                return [lookup[complement], index]

            lookup[number] = index

        return []


def main():

    numbers = [2, 7, 11, 15]
    target = 9

    result = TwoSum.find(numbers, target)

    print("Numbers:")
    print(numbers)

    print(f"\nTarget: {target}")

    if result:
        print(f"\nIndices: {result}")
        print(
            f"Values: {numbers[result[0]]} + "
            f"{numbers[result[1]]} = {target}"
        )
    else:
        print("\nNo solution found.")


if __name__ == "__main__":
    main()
