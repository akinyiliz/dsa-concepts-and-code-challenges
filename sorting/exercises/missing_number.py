'''
Write a function finds the “missing number” from an array of inte-
gers. That is, the array is expected to have all integers from 0 up to the
array’s length, but if one number is missing it should return it. As examples, the array, [5, 2, 4, 1, 0] is
missing the number 3, and the array, [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the
number 8.
Use sorting to write an implementation of this function that only takes
O(N log N). (There are even faster implementations, but we’re focusing on
using sorting as a technique to make code faster.)
'''


def missing_number(arr):
    sorted_arr = sorted(arr)

    for i in range(0, len(sorted_arr)):
        if sorted_arr[i] != i:
            return i

    return None


# Example Usage
print(missing_number([9, 3, 2, 5, 6, 7, 1, 0, 4])) #8
