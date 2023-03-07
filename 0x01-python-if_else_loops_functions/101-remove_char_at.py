#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        new_str = str
    else:
        new_str = str[:n]
        new_str += str[n+1:]
    return new_str
