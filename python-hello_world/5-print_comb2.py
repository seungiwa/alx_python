#!/usr/bin/python3
for word in range(100):
    # Print two digits with leading zeros if necessary
    print('{:02}'.format(word), end=", ")
    if word == 99:
        print(word, end="\n ")
