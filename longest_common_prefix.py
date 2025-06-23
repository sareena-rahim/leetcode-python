class Solution:
    def longestCommonPrefix(self, strs):
        #handle edge cases
        if not strs:
            return ''
        # Sort Strings - First and Last will have minimum common prefix
        sorted_list=sorted(strs)
        first=sorted_list[0]
        last=sorted_list[-1]
        min_length = min(len(first),len(last))
        prefix=''
        for i in range(min_length):
            if first[i]==last[i]:
                prefix=prefix+first[i]
            else:
                break #stop at the first difference
        return prefix
sol=Solution()
print(sol.longestCommonPrefix(["dog","racecar","car"]))