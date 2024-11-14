#Create a multiplication table for a list of numbers using nested for loops. For example, given [2, 3, 4], it should print a table showing each number multiplied by every other number
numbers = [2, 3, 4]
for i in range(10):
    for j in numbers:
            print(f"the product of {i} *{j} is {i*j}")
