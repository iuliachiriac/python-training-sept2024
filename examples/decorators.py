import functools


def decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(f"Function {func.__name__} got called with args={args} and "
              f"kwargs={kwargs}.")
        return func(*args, **kwargs)
    return inner


@decorator
def greet(name):
    print(f"Hello, {name}!")
# greet = decorator(greet)  # greet = decorator.<locals>.inner


greet("Anna")  # decorator.<locals>.inner("Anna")


@decorator
def decrement(nr, step=1):
    """Returns nr decremented by step"""
    return nr - step


nr = 1 + decrement(10) + decrement(14, 2) + decrement(10, step=3)
print(nr)

print(decrement.__name__, decrement.__doc__)
