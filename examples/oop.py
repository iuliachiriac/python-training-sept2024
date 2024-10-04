from datetime import date


class Person:
    count = 0  # class attribute

    def __init__(self, name, date_of_birth=None):
        self.name = name  # instance attribute
        self.date_of_birth = date_of_birth
        self._increment_count()

    @classmethod
    def _increment_count(cls):
        cls.count += 1

    @staticmethod
    def compute_age(date_of_birth):
        today = date.today()
        age = today.year - date_of_birth.year
        if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
            age -= 1
        return age

    def get_age(self):
        return self.compute_age(self.date_of_birth)

    def greet(self, greeting=None):
        greeting = greeting or "hello"
        print(f"{greeting.capitalize()}, I am {self.name}!")

    def __str__(self):
        return f"Person(name={self.name}, date_of_birth={self.date_of_birth})"

    def __lt__(self, other):
        return self.date_of_birth > other.date_of_birth

    def __iadd__(self, other):
        self.date_of_birth = date(self.date_of_birth.year - other,
                                  self.date_of_birth.month,
                                  self.date_of_birth.day)
        return self


if __name__ == "__main__":
    p1 = Person("Anna", date(1973, 5, 2))
    p2 = Person("Jane", date(2001, 6, 12))
    print(p1.name, p2.name, p2.date_of_birth, p1.__dict__, p2.__dict__)

    print(Person.count, p1.count, p1.count is Person.count)

    p1.greet('good morning')
    p2.greet()

    # Person.greet(p1, 'good morning')
    # Person.greet(p2)

    print(str(p1), p1, f'{p1}')

    print(f'{p1.name} is younger than {p2.name}:', p1 < p2)

    p1 += 2
    print(p1.date_of_birth)

    print(Person.compute_age(date(1918, 12, 1)))
    print(p1.get_age())
