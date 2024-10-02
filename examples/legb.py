X = 100
global_lst = []


def my_func(a):
    b = 2

    def inner(c):
        d = 22

        print("-- Inside inner --")
        print("Local names:", c, d)
        print("Enclosing names:", a, b, inner)
        print("Global names:", X, my_func, MyClass)
        print("Built-in names:", int, None, len, NameError)

    # X = 0  # shadowing
    # modifying global objects inside functions is not recommended
    # global_lst.append(10)  # change of global object
    # global_lst = ['afds', 'wfsd']  # redeclaration of global object

    inner(11)

    print("-- Inside my_func --")
    print("Local names:", a, b, inner)
    print("Global names:", X, my_func, MyClass)
    print("Built-in names:", int, None, len, NameError)


class MyClass:
    pass


# sum = 0  # shadowing
# print(sum)  # sum is global if defined above, built-in otherwise

my_func(1)

print("-- Global --")
print("Global names:", X, my_func, MyClass, global_lst)
print("Built-in names:", int, None, len, NameError)
