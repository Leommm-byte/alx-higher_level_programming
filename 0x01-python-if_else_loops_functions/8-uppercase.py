#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for letter in str:
        if ord(letter) in range(97, 123):
            str1 += "{letter}".format(letter=chr(ord(letter) - 32))
        else:
            str1 += letter
    print(str1)
