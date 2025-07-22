# Functional approach with map(), filter() & reduce()
#
# AUTHOR Sven Schrodt <sven@schrodt.club>
# SINCE 2025-01-28
# SEE https://book.pythontips.com/en/latest/map_filter.html
# SEE https://github.com/yasoob/intermediatePython/

from functools import reduce
# Mapping - map applies a function to each item of a given list. 
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(i, value)


def my_filter(x):
    return True if x < 0 else False

# Filtering - filter creates a list of items from an origin list, for which 
# a given function return True ()

lowest_to_highest = range(-5, 6) # (-5, -4 ..1, ..5)
for i in lowest_to_highest:
    print(i)
less_than_zero = list(filter(my_filter, lowest_to_highest)) ## function or lambda:
#less_than_zero = list(filter(lambda x: x < 0, lowest_to_highest))
print(less_than_zero == [-5, -4, -3, -2, -1])

# Output: [-5, -4, -3, -2, -1]

numbers = range (14)

even_numbers = list(filter(lambda x: x % 2 == 0 , numbers))
print(even_numbers)
even = [2, 4, 6, 10]
for i in even:
    assert(i in even_numbers)
    
product = 1
list = [1, 2, 3, 4, 5]
for num in list:
    product = product * num
    print(product)
print('____________________________________')
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)

