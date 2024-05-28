'''
Write a function that returns an array of all anagrams of a
given string. An anagram is a reordering of all the characters within a string.
For example, the anagrams of "abc" are:
["abc", "acb", "bac", "bca", "cab", "cba"]
'''


# SOLUTION 1
# import itertools


# def generate_anagrams(s):
#     # Generate all permutations of the input string
#     permutations = itertools.permutations(s)

#     # Convert permutations from tuples to strings and return as a list
#     anagrams = [''.join(p) for p in permutations]

#     return anagrams


# SOLUTION 2

def generate_anagrams(s):
    '''
    Helper function to recursively generate anagrams. It takes three arguments:
        - current: The current permutation being built.
        - remaining: The characters left to be added to the current permutation.
        - results: A list to store all the generated permutations.
    '''
    def permute(current, remaining, results):
        if len(remaining) == 0:
            results.append(current)
        else:
            for i in range(len(remaining)):
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i+1:]
                permute(new_current, new_remaining, results)

    results = []
    permute("", s, results)
    return results


# Example usage:
anagrams = generate_anagrams("abcd")
print(anagrams)
