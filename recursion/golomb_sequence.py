'''
Write a function uses recursion to calculate the Nth number from
a mathematical sequence known as the “Golomb sequence.”
The Golomb sequence is a special sequence of numbers where each number represents 
how many times that position number has appeared in the sequence up to that point.
'''


def golomb(n, memo={}):
    if n == 1:
        return 1

    if not memo.get(n):
        memo[n] = 1 + golomb(n - golomb(golomb(n-1)))

    return memo[n]


# Example Usage
print(golomb(11))
