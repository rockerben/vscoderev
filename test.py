

# create a list of 100 numbers from 0 to 99
numbers = list(range(100))

# create a list of even numbers from 0 to 99
even_numbers = [number for number in numbers if number % 2 == 0]

# print the list of even numbers
print(even_numbers)