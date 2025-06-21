class Solution:
    def is_palindrome(self, x: int):
        x=str(x)
        if x[::-1] == x:
            return True
        else:
            return False
sol = Solution()
print(sol.is_palindrome(242))