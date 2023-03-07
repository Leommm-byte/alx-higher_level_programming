#!/usr/bin/python3
for i in range(1, 100):
    if i % 10 > int(i / 10):
        if int(i / 10) == 8 and i % 10 == 9:
            print(i)
        else:
            print("{x}{y}".format(x=int(i / 10), y=i % 10), end=", ")
