

# create a list of 100 numbers from 0 to 99
numbers = [number for number in range(100)]
numbers1 = [number for number in range(100)]

# create a list of even numbers from 0 to 99
even_numbers = [number for number in numbers if number % 2 == 0]

# print the list of even numbers
print(even_numbers)

# create a list of odd numbers from 0 to 99
odd_numbers = [number for number in numbers if number % 2 != 0]

# print the list of odd numbers
print(odd_numbers)

# create a list of numbers from 0 to 99 that are divisible by 3
divisible_by_3 = [number for number in numbers if number % 3 == 0]
