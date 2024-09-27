''' Is Anagram - Easy
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.
'''


class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        hashS, hashT = {}, {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)

        for i in range(len(t)):
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        return hashS == hashT

    # OR

    def anotherIsAnagram(self, s: str, t: str):
        return sorted(s) == sorted(t)


sol = Solution()
print(sol.isAnagram("racecar", "carrace"))  # True

print(sol.isAnagram("jar", "jam"))  # False
