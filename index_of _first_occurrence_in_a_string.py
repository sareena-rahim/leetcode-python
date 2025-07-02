class Solution:
    def strStr(self, haystack: str, needle: str):
        if needle  in haystack:
            return haystack.index(needle)
        else:
            return -1

sol=Solution()
print(sol.strStr(haystack = "leetcode", needle = "leeto"))