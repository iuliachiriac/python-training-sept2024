"""This is a docstring"""

print("hello world")

x = -14
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

code_block = """total_minutes = 100
hours = total_minutes // 60
minutes = total_minutes % 60
print("Exercise 2")
print(hours, minutes)"""
print(code_block)

string_with_special_chars = "\n\t\"\'\\"
print(string_with_special_chars)
