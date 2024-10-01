# 1. Write an expression that returns True if x is strictly greater than 4.3 and
# smaller or equal to 7.9, or if it is 3, and try changing x to see if it works.
x = 6.5
print(4.3 < x <= 7.9 or x == 3)

# 2. Given two integers, x and y, create a boolean which is True only if one of
# them is 100 or if their sum is 100.
x = 80
y = 20
print(x == 100 or y == 100 or x + y == 100)

# 3. Try out the following operations in the Python shell and explain the output:
# >>> True and 'True'
# the first operand (True) evaluates as True, so the second operand ('True')
# is returned
# >>> 0 or False
# the first operand (0) evaluates as False, so the second operand (False)
# is returned

# 4. Let's assume that variable age was initialized with a value returned by a
# function that is generally a number, but can also be None. How can you make
# sure that age is always a number (default value 0)?
age = 10
print(age)
age = None
print(age or 0)
