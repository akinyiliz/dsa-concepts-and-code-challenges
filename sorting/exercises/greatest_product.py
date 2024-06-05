'''
Given an array of positive numbers, write a function that returns the
greatest product of any three numbers. The approach of using three
nested loops would clock in at O(N^3), which is very slow. Use sorting to
implement the function in a way that it computes at O(N log N) speed.
(There are even faster implementations, but we’re focusing on using
sorting as a technique to make code faster.)

If we sort the numbers, we know that the three greatest numbers will be
at the end of the array, and we can just multiply them together. The
sorting will take O(N log N):
'''


def greatest_product_of_three(array):
    sorted_arr = sorted(array)

    arr_length = len(sorted_arr)

    return sorted_arr[arr_length - 1] * sorted_arr[arr_length - 2] * sorted_arr[arr_length - 3]


# Example Usage:
print(greatest_product_of_three([2, 4, 1, 8, 9, 6]))
# 1, 2, 4, 6, 8, 9,
# 6*8*9 = 432
