#!/usr/bin/python3
if __name__ == "__main__":
    import sys

add = 0
count = len(sys.argv) - 1
if count == 0:
    print(0)
elif count == 1:
    print(sys.argv[1])
else:
    for i in range(count):
        add += int(sys.argv[i + 1])
    print(add)
