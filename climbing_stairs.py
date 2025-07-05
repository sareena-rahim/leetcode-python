class Solution:
    def climbStairs(self, n):
        """
        Calculate the number of distinct ways to climb n stairs.
        You can climb either 1 or 2 steps at a time.

        Args:
            n (int): Number of stairs to climb

        Returns:
            int: Number of distinct ways to climb the stairs
            str: Error message for invalid input
        """
        # Handle edge cases
        if n < 0:
            return 'Incorrect Input'
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev = 0
        curr = 1


        for i in range(n):
            next_value = prev + curr
            prev = curr
            curr = next_value

        return curr
sol=Solution()
print(sol.climbStairs(5))