'''
The Fibonacci sequence is a mathematical sequence of numbers that goes
like this until infinity:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
This sequence begins with the numbers 0 and 1, and each subsequent
number is the sum of the previous two numbers of the sequence. For example,
the number 55 was computed because it is the sum of the previous two
numbers, which are 21 and 34.

The following Python function returns the Nth number in the Fibonacci
sequence.
'''


# def fib(n):
#     if n == 0 or n == 1:
#         return n

#     return fib(n-2) + fib(n-1)


'''
In the above function, the recursive function is being called twice which isn't efficient.
A function calling itself twice can easily lead us down the road to O(2^N) which is slow

First technique to solve this is by Memoization
Memoization reduces recursive calls by remembering previously computed functions.

In our Fibonacci example, the first time fib(3) is called, the function does its
computation and returns the number 2. However, before moving on, the
function stores this result inside a hash table. The hash table will look
something like this: {3: 2}
This indicates that the result of fib(3) is the number 2.
'''


# def fib(n, memo={}):
#     if n == 0 or n == 1:
#         return n

#     #  Before making any recursive calls, our code first checks to see whether fib(n) has already been calculated for the given n:
#     if not memo.get(n):
#       # Only if the calculation for n has not yet been made do we proceed with the calculation:
#         memo[n] = fib(n-2, memo) + fib(n-1, memo)

#     return memo[n]


'''
With Memoization, we can see that for N, we make (2N) - 1 calls. Since in Big O we drop the
constants, this is an O(N) algorithm.
This is an incredible improvement over O(2^N). Go memoization!
'''


'''
The second technique, known as going bottom-up, is a lot less fancy and may
not even seem like a technique at all. All going bottom-up means is to ditch
recursion and use some other approach (like a loop) to solve the same problem.

The reason that going bottom-up is considered part of dynamic programming
is because dynamic programming means taking a problem that could be solved
recursively and ensure that it doesn’t make duplicate calls for overlapping
subproblems. Using iteration (that is, loops) instead of recursion is, technically,
a way to achieve this.
'''


def fib(n):
    if n == 0:
        return 0

    # a and b start with the first two numbers in the series, respectively:
    a = 0
    b = 1

    # Loop from 1 until n:
    for i in range(1, n):
        # a and b each move up to the next numbers in the series.
        # Namely, b becomes the sum of b + a, and a becomes what b used to be.
        # We utilize a temporary variable to make these changes:
        temp = a
        a = b
        b = temp+a

    return b


'''
Because our code is a simple loop from 1 to N, our code takes N steps. Like
the memoization approach, it’s O(N).
'''

# Example Usage:
print(fib(15))
