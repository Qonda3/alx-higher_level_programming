#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = (-1 * number) % 10
elif number >= 0:
    last_digit = number % 10
message = f"Last digit of {number} is {last_digit} and is"
if last_digit > 5:
    print(f"{message} greater than 5")
elif last_digit == 0:
    print(f"{message} 0")
else:
    print(f"{message} less than 6 and not 0")
