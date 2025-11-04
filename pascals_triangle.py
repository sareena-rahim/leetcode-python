class Solution:
    def generate(self, numRows: int):
        large_list = []
        for i in range(numRows):
            small_list = []
            num = 1
            for j in range(i + 1):
                small_list.append(num)
                num = num * (i - j) // (j + 1)
            large_list.append(small_list)
        return large_list



sol=Solution()
result=sol.generate(5)