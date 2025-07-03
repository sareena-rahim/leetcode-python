class Solution:
    def lengthOfLastWord(self, s: str):
        """
              Returns the length of the last word in a string.

              Args:
                  s (str): Input string that may contain leading/trailing spaces

              Returns:
                  int: Length of the last word
              """
        # Remove leading and trailing whitespace, then split by spaces
        words=s.strip().split(' ')
        # Return the length of the last word
        return len(words[-1])


sol=Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))