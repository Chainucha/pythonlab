# Program using user defined exception class that will ask the user to enter a number
# until he guesses a stored number correctly. To help them figure it out, a hint is
# provided whether their guess is greater than or less than the stored number using user
# defined exceptions.

import random


class Error(Exception):
    pass


class ValueTooSmallError(Error):
    pass


class ValueTooLargeError(Error):
    pass


lower = int(input("Enter Lower bound:- "))  # Taking Inputs
upper = int(input("Enter Upper bound:- "))
x = random.randint(lower, upper)  # generating random number
while True:
    try:
        guess = int(input("Guess a number:- "))  # taking guessing number as input
        if x == guess:
            print("Congratulations you guessed the correct number")
            break
        elif x > guess:
            raise ValueTooSmallError
        elif x < guess:
            raise ValueTooLargeError
    except ValueTooSmallError:
        print("This value is too small, try again!\n")
    except ValueTooLargeError:
        print("This value is too large, try again!\n")
