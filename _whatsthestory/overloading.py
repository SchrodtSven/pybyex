# As we know, the + operator can:
# - perform addition on two numbers, 
# - merge two lists, or
# - concatenate two strings.
# @since 2024-12-11
# @author Sven Schrodt
    
# In fact, the + operator internally calls the __add__() method to add integers and floats.


# Here are some of the special functions available in Python:

# Function	Description
# __init__()	Initialize the attributes of the object.
# __str__()	Returns a string representation of the object.
# __len__()	Returns the length of the object.
# __add__()	Adds two objects.
# __call__()	Call objects of the class like a normal function.


# Similarly, we can overload other operators as well. The special function that we need to implement 
# is tabulated below.
#
#Similarly, we can overload other operators as well. The special function that we need to implement is tabulated below.

# Operator	Expression	Internally
# Addition	p1 + p2	p1.__add__(p2)
# Subtraction	p1 - p2	p1.__sub__(p2)
# Multiplication	p1 * p2	p1.__mul__(p2)
# Power	p1 ** p2	p1.__pow__(p2)  
# Division	p1 / p2	p1.__truediv__(p2)
# Floor Division	p1 // p2	p1.__floordiv__(p2)
# Remainder (modulo)	p1 % p2	p1.__mod__(p2)
# Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
# Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
# Bitwise AND	p1 & p2	p1.__and__(p2)
# Bitwise OR	p1 | p2	p1.__or__(p2)
# Bitwise XOR	p1 ^ p2	p1.__xor__(p2)
# Bitwise NOT	~p1	p1.__invert__()

# comparison operators

#__eq__(self, other)
#Defines behavior for the equality operator, ==.
#__ne__(self, other)
#Defines behavior for the inequality operator, !=.
#__lt__(self, other)
#Defines behavior for the less-than operator, <.
#__gt__(self, other)
#Defines behavior for the greater-than operator, >.
#__le__(self, other)
#Defines behavior for the less-than-or-equal-to operator, <=.
#__ge__(self, other)
#Defines behavior for the greater-than-or-equal-to operator, >=.


