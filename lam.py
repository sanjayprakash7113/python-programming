
square = lambda x: x ** 2
print(square(5))

add = lambda a, b: a + b
print(add(10, 20))

check = lambda n: "positive" if n > 0 else "negative"
print(check(-4))

# list for map, filter, reduce
nums = [2, 4, 6, 8, 10]

# map -> cube each number
cubes = list(map(lambda x: x ** 3, nums))
print(cubes)

# filter -> keep only numbers greater than 5
greater = list(filter(lambda x: x > 5, nums))
print(greater)

# reduce -> multiply all numbers
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(product)
