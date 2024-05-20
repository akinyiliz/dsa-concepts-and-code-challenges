# Write a function called sum that sums up all the numbers in
# a given array. For example, if we pass the array, [1, 2, 3, 4, 5] into the function,
# it’ll return 15, which is the sum of those numbers.

def sum(array):
    if len(array) == 1:
        return array[0]

    return array[0] + sum(array[1:])


print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
