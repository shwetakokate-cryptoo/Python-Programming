# Bubble Sort Algorithm in Python

# Bubble Sort repeatedly compares adjacent
# elements and swaps them if they are in
# the wrong order.

# Example:
# Input : 64 34 25 12 22 11 90
# Output: 11 12 22 25 34 64 90


# Function to Perform Bubble Sort

def bubble_sort(numbers):

    n = len(numbers)

    # Traverse through all array elements
    for i in range(n):

        swapped = False

        # Last i elements are already sorted
        for j in range(0, n - i - 1):

            if numbers[j] > numbers[j + 1]:

                # Swap elements
                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )

                swapped = True

        # Stop if no swapping happened
        if not swapped:
            break

    return numbers


# Main Program

def main():

    print("===================================")
    print("         BUBBLE SORT")
    print("===================================")

    while True:

        try:
            # Input array
            user_input = input(
                "\nEnter numbers separated by spaces: "
            )

            numbers = list(map(int, user_input.split()))

            if len(numbers) == 0:
                print("Please enter at least one number.")
                continue

        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue

        # Sort array
        sorted_numbers = bubble_sort(numbers.copy())

        # Display results
        print("\nOriginal Array:", numbers)
        print("Sorted Array  :", sorted_numbers)

        # Continue?
        again = input(
            "\nSort another array? (yes/no): "
        ).lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break



main()
