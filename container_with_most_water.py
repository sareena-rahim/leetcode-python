class Solution:
    def maxArea(self, height) -> int:
        left=0
        right=len(height)-1

        maximum_water = 0

        while left<right:
            smaller=min(height[left],height[right])
            quantity=smaller*(right-left)
            if quantity>maximum_water:
                maximum_water = quantity
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maximum_water
sol = Solution()
result=sol.maxArea([1,8,6,2,5,4,8,3,7])