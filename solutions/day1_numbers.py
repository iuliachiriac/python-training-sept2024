# 1. Declare a variable called `celsius_temp` and assign it a temperature in
# Celsius as a float. Convert the temperature to Fahrenheit using the formula:
# `Fahrenheit = (Celsius * 9/5) + 32`. Round the result to a one decimal number
# and store it in a variable called `fahrenheit_temp`. Print the Fahrenheit
# temperature.
celsius_temp = 15.3
fahrenheit_temp = (celsius_temp * 9 / 5) + 32
fahrenheit_temp = round(fahrenheit_temp, 1)
print(fahrenheit_temp)

# 2. Define a variable called `total_minutes` and assign it a value chosen by
# you between 0 and 1440. Consider this to be the number of minutes passed
# after midnight. What time would a digital 24h clock show? Compute and display
# the two values: `hour` and `minute`.
# For example, if total_minutes = 150, then 150 minutes have passed since
# midnight - i.e. now it's 2:30 am. So the program should print 2 30.
total_minutes = 150
minutes_in_hour = 60

print('Time on digital clock:',
      total_minutes // minutes_in_hour,
      total_minutes % minutes_in_hour)

print('Time on digital clock:',
      *divmod(total_minutes, minutes_in_hour))

# 3. Given an integer number, print its last digit.
x = 7343
print(f'Last digit of {x}:', x % 10)

# 4. Given a three-digit number. Find the sum of its digits.
x = 852
print(f'Sum of digits of {x}:', x // 100 + x // 10 % 10 + x % 10)
