#!/usr/bin/python3
def fizzbuzz():
    """Prints numbers from 1 to 100 with Fizz for multiples of 3,
    Buzz for multiples of 5,
    and FizzBuzz for multiples of both, separated by spaces."""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
