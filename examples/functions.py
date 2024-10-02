def greet():
    """Prints a greeting message"""
    print('Hello world!')


def get_greeting():
    return 'hello world'


greet()
greeting = get_greeting()
print(greeting, len(greeting))


def decrement(nr, step=1):
    if step is None:
        return
    return nr - step


print(decrement(10))
print(decrement(10, 2))

print(decrement(nr=10, step=3))
print(decrement(step=3, nr=10))

print(decrement(10, step=None))


def varargs(nr, *args, step=1, **kwargs):
    print(nr, step)
    print(args, type(args))
    # for arg in args:
    #     if arg == 20:
    #         return
    print(kwargs, type(kwargs))
    print()


varargs(10, step=2)
varargs(10, 20)
varargs(10, 'hello', 12.45, 'test', 10)

varargs(10, name='Anna', age=20)
varargs(10, 20, 30, name='Anna', age=20)

# name
# Out[599]: 'Andrei'
# age
# Out[600]: 0
# f'{name} is {age} years old'
# Out[601]: 'Andrei is 0 years old'
# '{0} is {1} years old'.format(name, age)
# Out[602]: 'Andrei is 0 years old'
# '{} is {} years old'.format(name, age)
# Out[603]: 'Andrei is 0 years old'
# '{0} is {1} years old. {0} is a baby.'.format(name, age)
# Out[604]: 'Andrei is 0 years old. Andrei is a baby.'
# '{name} is {age} years old. {name} is a baby.'.format(name='Ana', age=1)
# Out[605]: 'Ana is 1 years old. Ana is a baby.'
# '{name} is {age} years old. {name} is a baby.'.format(name=name, age=age)
# Out[606]: 'Andrei is 0 years old. Andrei is a baby.'


# Duck typing
def concatenate(*args):
    if not args:
        return
    result = args[0]
    for arg in args[1:]:
        result += arg
    return result


print(concatenate(1, 2, 3, 7, 12, 5))
print(concatenate('hello', ' ', 'world', '!'))
print(concatenate([3, 6, 7], [8, 3, 2]))
