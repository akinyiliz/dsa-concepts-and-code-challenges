# Write a reverse function that reverses
# a string. So, if the function accepts the argument "abcde", it’ll return "edcba".

def reverse(string):
    if len(string) == 1:
        return string[0]

    return reverse(string[1:]) + string[0]


print(reverse("abcde"))
