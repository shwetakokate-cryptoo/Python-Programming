# Selection Sort Algorithm in Python

# Selection Sort repeatedly finds the
# smallest element from the unsorted part
# of the array and places it at the correct position.

# Example:
# Input : 64 25 12 22 11
# Output: 11 12 22 25 64

# Function to Perform Selection Sort

def selection_sort(numbers):

    n = len(numbers)

    # Traverse through all array elements
    for i in range(n):

        # Assume current position has minimum element
        min_index = i

        # Find actual minimum element
        for j in range(i + 1, n):

            if numbers[j] < numbers[min_index]:
                min_index = j

        # Swap minimum element with current element
        numbers[i], numbers[min_index] = (
            numbers[min_index],
            numbers[i]
        )

    return numbers



def main():

    print("===================================")
    print("        SELECTION SORT")
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
        sorted_numbers = selection_sort(numbers.copy())

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
