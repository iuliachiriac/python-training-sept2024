age = 20

if age is None:
    age = 0
    print("inside if")
elif age < 18:
    print("Minor")
else:
    print("Major")

print(age)
