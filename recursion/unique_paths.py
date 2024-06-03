'''
This problem is known as the “Unique Paths” problem: Let’s say you have
a grid of rows and columns. Write a function that accepts a number of rows
and a number of columns, and calculates the number of possible “shortest”
paths from the upper-leftmost square to the lower-rightmost square.
'''


# def unique_paths(rows, columns):
#     if rows == 1 or columns == 1:
#         return 1

#     return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)


''' Improve efficiency using Memoization '''


def unique_paths(rows, columns, memo={}):
    if rows == 1 or columns == 1:
        return 1

    if not memo.get("rc"):
        memo["rc"] = unique_paths(
            rows - 1, columns, memo) + unique_paths(rows, columns - 1, memo)

    return memo["rc"]


# Example Usage
print(unique_paths(3, 3))
