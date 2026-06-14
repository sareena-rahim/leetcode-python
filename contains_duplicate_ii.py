class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        num_dict={}
        for i in range(len(nums)):
            if nums[i] in num_dict and abs(i-num_dict[nums[i]]) <= k:
                return True
            num_dict[nums[i]]=i
        else:
            return False

sol = Solution()
print(sol.containsNearbyDuplicate([1,2,3,1,2,3],2))
