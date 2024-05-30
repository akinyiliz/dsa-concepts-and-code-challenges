'''
Use recursion to write a function that accepts an array of numbers and
returns a new array containing just the even numbers. [2,5,1,7,6] => [2,6]
'''


def even_numbers(arr):
    if len(arr) == 0:
        return []

    even_numbers_of_remainder = even_numbers(arr[1:])

    if arr[0] % 2 == 0:
        return [arr[0]] + even_numbers_of_remainder
    else:
        return even_numbers_of_remainder


# Example Usage:
print(even_numbers([2, 5, 1, 7, 6]))
