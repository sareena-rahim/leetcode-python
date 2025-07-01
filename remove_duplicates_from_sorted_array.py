class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[k]:
                k += 1
                nums[k] = nums[j]

        return k + 1


sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))