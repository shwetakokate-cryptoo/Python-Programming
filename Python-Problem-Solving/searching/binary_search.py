# Binary Search Algorithm in Python

# Binary Search works only on SORTED arrays.
# It repeatedly divides the search space in half
# until the target element is found.

# Example:
# Array : 10 20 30 40 50 60
# Target: 40
# Output: Element found at index 3

# Function to Perform Binary Search

def binary_search(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:

        # Find middle index
        mid = (left + right) // 2

        # Target found
        if numbers[mid] == target:
            return mid

        # Search right half
        elif numbers[mid] < target:
            left = mid + 1

        # Search left half
        else:
            right = mid - 1

    return -1


# Main Program

def main():

    print("===================================")
    print("        BINARY SEARCH")
    print("===================================")

    while True:

        try:
            # Input sorted array
            user_input = input(
                "\nEnter SORTED numbers separated by spaces: "
            )

            numbers = list(map(int, user_input.split()))

            if len(numbers) == 0:
                print("Please enter at least one number.")
                continue

            target = int(
                input("Enter number to search: ")
            )

        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue

        # Perform search
        result = binary_search(numbers, target)

        # Display result
        if result != -1:
            print(
                f"\nElement found at index {result}"
            )
        else:
            print("\nElement not found.")

        # Continue?
        again = input(
            "\nSearch another number? (yes/no): "
        ).lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break



main()
