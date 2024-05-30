'''
Write a recursive function that finds the greatest number from an array.
'''

'''
ATTEMPT 1
If you look carefully, you’ll note that our code contains the phrase, 
max(array[1, array.length - 1]) twice, once in each half of the conditional statement.
The problem with this is that each time we mention max(array[1, array.length - 1]),
we trigger an entire avalanche of recursive calls.
'''


# def max(arr):
#     # Base case - if the array has only one element, it is
#     # by definition the greatest number:
#     if len(arr) == 1:
#         return arr[0]

#     # Compare the first element with the greatest element from the remainder of the array.
#     # If the first element is greater, return it as the greatest number:
#     if arr[0] > max(arr[1:]):
#         return arr[0]
#     # Otherwise, return the greatest number from the remainder of the array:
#     else:
#         return max(arr[1:])


'''
ATTEMPT 2 - IMPROVED VERSION
There’s an easy way to eliminate all these extra recursive calls.
We’ll call max only once within our code, and save the result to a variable:
'''


def max(arr):
    if len(arr) == 1:
        return arr[0]

    # Calculate the max of the remainder of the array and store it inside a variable:
    max_of_remainder = max(arr[1:])

    # Comparison of first number against this variable:
    if arr[0] > max_of_remainder:
        return arr[0]
    else:
        return max_of_remainder


# Example Usage:
print(max([1, 2, 3, 4]))


'''
This is a powerful lesson: avoiding extra recursive calls is key to keeping
recursion fast. What at first glance was a very small change to our code—the
mere storing of a computation in a variable—ended up changing the speed
of our function from O(2N) to O(N).
'''
