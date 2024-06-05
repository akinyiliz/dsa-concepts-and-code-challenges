'''
Write three different implementations of a function that finds the greatest
number within an array. Write one function that is O(N log N), and one that is O(N).
'''


# O(N log N)

# def greatest_number(arr):
#     sorted_arr = sorted(arr)

#     return sorted_arr[-1]


# O(N)
def greatest_number(arr):
    greatest_num = arr[0]

    for i in range(0, len(arr)):
        if arr[i] > greatest_num:
            greatest_num = arr[i]

    return greatest_num


# Example Usage
print(greatest_number([5, 8, 9, 2, 4, 1]))  # 9
