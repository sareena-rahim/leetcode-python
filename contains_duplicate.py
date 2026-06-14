class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
                break
            seen.add(num)
        else:
            return False
sol = Solution()
print(sol.containsDuplicate([1,2,3,3,5]))