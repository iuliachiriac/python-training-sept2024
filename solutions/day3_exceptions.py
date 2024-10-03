# Write a program to read two numbers: x and y from standard input and print
# the result of x / y. If the user inputs invalid data, display an error message
# and exit gracefully.

try:
    nr1 = int(input("Type first number: "))
    nr2 = int(input("Type second number: "))
    result = nr1 / nr2
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print('Cannot divide by 0')
else:
    print(f'Result = {result}. Good job!')

# Modify the previous program so that it asks the user to re-enter data until
# valid.

# Loop
while True:
    try:
        nr1 = int(input("Type first number: "))
        nr2 = int(input("Type second number: "))
        result = nr1 / nr2
    except ValueError:
        print("Not a number!")
    except ZeroDivisionError:
        print('Cannot divide by 0')
    else:
        print(f'Result = {result}. Good job!')
        break


# Recursive function
def compute_division():
    try:
        first = int(input("Type first number: "))
        second = int(input("Type second number: "))
        res = first / second
    except ValueError:
        print("Not a number!")
        compute_division()
    except ZeroDivisionError:
        print('Cannot divide by 0')
        compute_division()
    else:
        print(f'Result = {res}. Good job!')


compute_division()
