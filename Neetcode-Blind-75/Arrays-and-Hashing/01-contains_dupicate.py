''' Duplicate Integer - Easy
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
'''


class Solution:
    def hasDuplicate(self, nums):
        hash_set = set()

        for i in range(len(nums)):
            if nums[i] in hash_set:
                return True
            hash_set.add(nums[i])
        return False


newD = Solution()
print(newD.hasDuplicate([1, 2, 3, 1]))
