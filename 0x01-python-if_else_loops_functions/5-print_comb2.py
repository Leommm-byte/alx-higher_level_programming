#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print(i)
    else:
        print("{x}{y}".format(x=int(i / 10), y=i % 10), end=", ")
