#!/usr/bin/python3
for word in range(0, 9):
    #Iterating through all possible combinations of two digits, excluding duplicates like "01" and "10."
    for word1 in range(word + 1, 10):
        print("{}{}".format(word, word1), end=", " if (word < 8) else "\n")
        
