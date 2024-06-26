'''
Use recursion to write a function that accepts an array of strings and
returns the total number of characters across all the strings. For example,
if the input array is ["ab", "c", "def", "ghij"], the output should be 10 since there
are 10 characters in total.
'''


def character_count(arr):
    if len(arr) == 0:
        return 0

    return len(arr[0]) + character_count(arr[1:])


# Example Usage:
chars = character_count(["ab", "c", "def", "ghij", "klm", "n"])
print(chars)
