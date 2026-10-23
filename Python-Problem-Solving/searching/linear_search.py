# Linear Search Algorithm in Python

# Linear Search checks each element
# one by one until the target element
# is found or the list ends.

# Example:
# Array : 10 20 30 40 50
# Target: 30
# Output: Element found at position 3

# Function to Perform Linear Search

def linear_search(numbers, target):

    # Traverse the list
    for index in range(len(numbers)):

        if numbers[index] == target:
            return index

    return -1


# Main Program

def main():

    print("===================================")
    print("        LINEAR SEARCH")
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

            # Input target value
            target = int(input("Enter number to search: "))

        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue

        # Search element
        result = linear_search(numbers, target)

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
