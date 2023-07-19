#!/usr/bin/python3
for num in range(100):
        #end = ", " if num is less than 99
        print("{:02}".format(num), end=", " if num < 99 else "\n")

