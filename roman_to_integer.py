class Solution:
    def romanToInt(self, s: str):
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i > 0 and symbols[s[i]] > symbols[s[i - 1]]:
                ans = ans + symbols[s[i]] - 2 * symbols[s[i - 1]]
            else:
                ans = ans + symbols[s[i]]
        return ans


sol = Solution()
print(sol.romanToInt('X'))

