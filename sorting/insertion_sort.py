# Insertion Sort Algorithm in Python

# Insertion Sort builds the sorted array
# one element at a time by inserting each
# element into its correct position.

# Example:
# Input : 12 11 13 5 6
# Output: 5 6 11 12 13

# Function to Perform Insertion Sort
def insertion_sort(numbers):

    # Traverse from second element
    for i in range(1, len(numbers)):

        key = numbers[i]
        j = i - 1

        # Move elements greater than key
        # one position ahead
        while j >= 0 and numbers[j] > key:

            numbers[j + 1] = numbers[j]
            j -= 1

        # Insert key at correct position
        numbers[j + 1] = key

    return numbers


# Main Program

def main():

    print("===================================")
    print("        INSERTION SORT")
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
        sorted_numbers = insertion_sort(numbers.copy())

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
