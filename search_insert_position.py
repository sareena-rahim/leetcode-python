class Solution:
    def searchInsert(self, nums:list, target):
        """
            Find the index where target should be inserted in a sorted array.

            Args:
                nums: Sorted array of integers
                target: Target value to search for or find insertion position

            Returns:
                Index where target is found or should be inserted
            """
        start=0
        end=len(nums)-1
        while start<=end:
            mid =(start+end)//2
            if nums[mid] ==target:
                return mid
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        # If not found, start is the insertion position
        return start
sol=Solution()
print(sol.searchInsert([1,2,3,4],5))