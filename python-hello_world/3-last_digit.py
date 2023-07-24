#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

#get the last digit of a random number
lastDigit = abs(number) % 10

#checks if the last number is negative
if number < 0:
    lastDigit *= -1

#Determine the output of the condition
if lastDigit > 5:
    print('Last digit of {} is {} and is greater than 5'.format(number, lastDigit))
elif lastDigit == 0:
    print('Last digit of {} is {} and is 0'.format(number, lastDigit))
else:
    print('Last digit of {} is {} and is less than 6 and not 0'.format(number, lastDigit))
