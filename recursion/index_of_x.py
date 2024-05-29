'''
Use recursion to write a function that accepts a string and returns the
first index that contains the character “x.” For example, the string,
"abcdefghijklmnopqrstuvwxyz" has an “x” at index 23. To keep things simple,
assume the string definitely has at least one “x.”
'''


def index_of_x(str):
    if str[0] == "x":
        return 0

    return index_of_x(str[1:]) + 1


# Example Usage:
print(index_of_x("abcdefghijklmnopqrstuvwxyz"))
