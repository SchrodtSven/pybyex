# generators .py
# Example generators in Python
#
# AUTHOR Sven Schrodt <sven@schrodt.club>
# SINCE 2025-07.10

""" Generators in Python are a convenient way to create iterators. They allow us to iterate through a sequence of values which means, values are generated 
    on the fly and not stored in memory, which is especially useful for large datasets or infinite sequences.
"""

def count_up_to(max_value):
    current = 1
    while current <= max_value:
        yield current
        current += 1

# Using the generator
counter = count_up_to(5)
for number in counter:
    print(number)
    
    
    
    
# Using Generator Expressions

""" Generator expressions provide a compact way to create generators. They use a syntax similar to list 
    comprehensions but used parentheses i.e. "{}" instead of square brackets i.e. 
"""

gen_expr = (x * x for x in range(1, 6))

for value in gen_expr:
    print(value)
