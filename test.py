import random

# Generate a list of 10 random integers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

print("Original list:", random_numbers)

# Filter the list to include only even numbers
even_numbers = [num for num in random_numbers if num % 2 == 0]

print("Even numbers:", even_numbers)