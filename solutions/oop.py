from datetime import date


class Person:
    count = 0  # class attribute

    def __init__(self, name, date_of_birth=None):
        self.name = name  # instance attribute
        self.date_of_birth = date_of_birth
        Person.count += 1

    def greet(self, greeting=None):
        greeting = greeting or "hello"
        print(f"{greeting.capitalize()}, I am {self.name}!")


if __name__ == "__main__":
    p1 = Person("Anna")
    p2 = Person("Jane", date(1973, 5, 2))
    print(p1.name, p2.name, p2.date_of_birth, p1.__dict__, p2.__dict__)

    print(Person.count, p1.count, p1.count is Person.count)

    p1.greet('good morning')
    p2.greet()

    # Person.greet(p1, 'good morning')
    # Person.greet(p2)
