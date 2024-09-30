"""This is a docstring"""

print("hello world")

x = -10
print(x)

# explicit line joining
sentence = "If we have a long logical line, we can split it into physical \
lines by using the backslash at the end of the line so that Python\
 understands that the next physical line should be considered as \
part of the current logical line."
print(sentence)

# implicit line joining
print(
    x,
    sentence
)

if x > 0:
    print("gt")
    print("still inside if")

print("outside if")
