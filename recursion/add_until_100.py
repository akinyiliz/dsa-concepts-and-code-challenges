'''
Write a function accepts an array of numbers and returns the sum,
as long as a particular number doesn’t bring the sum above 100. If adding
a particular number will make the sum higher than 100, that number is
ignored.
'''


def add_until_100(array):
    if len(array) == 0:
        return 0

    sum_of_remaining_numbers = add_until_100(array[1:])

    if array[0] + sum_of_remaining_numbers > 100:
        return sum_of_remaining_numbers

    return array[0] + sum_of_remaining_numbers


# Example Usage:
print(add_until_100([1, 5, 8, 35, 70, 30]))
