class Solution:

    def getRow(self,numRows):
        res=[[1]]
        if numRows==0:
            return [1]
        for i in range(numRows):
            temp=[0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])

            res.append(row)
        return res[-1]
sol=Solution()
result=sol.getRow(3)