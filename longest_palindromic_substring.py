class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest={'':0}
        last=len(s)-1

        for i in range(len(s)):
            if last-i+1 < max(longest.values()):

                break


            for j in range(i+1,len(s)+1):
                new_word=s[i:j+1]
                left = 0
                right = len(new_word)-1
                if len(new_word)==1:
                    longest[new_word]=1

                while left<right:
                    if new_word[left]!=new_word[right]:
                        break
                    left+=1
                    right-=1

                else:
                    longest[new_word]=len(new_word)
        return max(longest,key=longest.get)

sol=Solution()
result=sol.longestPalindrome("babad")
print(result)
        