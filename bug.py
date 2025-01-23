def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage with an empty list
average = calculate_average([])
print(f"Average: {average}")

# Example usage with a list of numbers
 numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"Average: {average}")

# Example with ZeroDivisionError
# numbers = []
# average = calculate_average(numbers)
# print(f"Average: {average}")