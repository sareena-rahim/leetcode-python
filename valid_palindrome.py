import string
class Solution:
    def isPalindrome(self,word):
        clean_word=' '.join(char.lower() for char in word if char not in string.punctuation).split()
        clean_joined=' '.join(clean_word)
        if len(clean_joined)==1 or clean_joined.strip()=='':

            return True

        for i in range((len(clean_word)//2)+1):
            if clean_word[i]!=clean_word[-i-1]:

                return False
        return True

sol=Solution()
print(sol.isPalindrome("race a car"))