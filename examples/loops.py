nr = 2456469
digit_sum = 0

while nr:  # while nr != 0
    last_digit = nr % 10
    digit_sum += last_digit
    nr //= 10

print(digit_sum)

for i in range(10, 1, -2):
    print(i)

for i in range(10, 1, -2):
    if i == 4:
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
