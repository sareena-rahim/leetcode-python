class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR each number
        return result


sol=Solution()
result=sol.singleNumber([4,1,2,1,2])