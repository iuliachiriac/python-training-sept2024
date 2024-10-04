from datetime import date
import random


class Person:
    count = 0  # class attribute
    MIN_YEAR = 1900

    def __init__(self, name, date_of_birth=None):
        self.name = name  # instance attribute
        self.date_of_birth = date_of_birth
        self._increment_count()

    @property
    def date_of_birth(self):  # getter
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):  # setter
        if isinstance(value, date) and value.year >= self.MIN_YEAR:
            self._date_of_birth = value
        else:
            raise ValueError(f"Invalid value for date_of_birth: {value}")

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

    @property
    def age(self):  # computed attribute
        return self.compute_age(self._date_of_birth)

    def greet(self, greeting=None):
        greeting = greeting or "hello"
        print(f"{greeting.capitalize()}, I am {self.name}!")

    def __str__(self):
        return f"Person(name={self.name}, date_of_birth={self._date_of_birth})"

    def __lt__(self, other):
        return self._date_of_birth > other.date_of_birth

    def __iadd__(self, other):
        self._date_of_birth = date(self._date_of_birth.year - other,
                                  self._date_of_birth.month,
                                  self._date_of_birth.day)
        return self


class Student(Person):
    count = 0

    def __init__(self, name, university, date_of_birth):
        super().__init__(name, date_of_birth)
        self.university = university

    def greet(self, greeting="hi"):
        print(f"{greeting.capitalize()}! My name is {self.name} and I study at "
              f"{self.university}")

    def get_grade(self, subject):
        return random.randint(2, 10)


if __name__ == "__main__":
    p1 = Person("Anna", date(1973, 5, 2))
    p2 = Person("Jane", date(2001, 6, 12))

    print(p1.name, p2.name, p2.date_of_birth, p1.__dict__, p2.__dict__)
    print(Person.count, p1.count, p1.count is Person.count)

    p1.greet('good morning')
    p2.greet()
    breakpoint()
    # Person.greet(p1, 'good morning')
    # Person.greet(p2)

    print(str(p1), p1, f'{p1}')

    print(f'{p1.name} is younger than {p2.name}:', p1 < p2)

    p1 += 2
    print(p1.date_of_birth)

    print(Person.compute_age(date(1918, 12, 1)))
    print(f"{p1.name} is {p1.age} years old.")

    print(p1.date_of_birth)  # get
    try:
        p1.date_of_birth = date(1890, 12, 1)  # set
    except ValueError as ex:
        print(ex)
    # del p1.date_of_birth  # delete

    s1 = Student("Mike Addams", "MIT", date(2005, 9, 20))
    print(s1.age, s1.name, s1.university)
    s1.greet()
    print(s1.get_grade("Math"))

    print(Person.count, Student.count)
