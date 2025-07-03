class Solution:
    def isValid(self, s):
        stack = []

        #closing brackets to their corresponding opening brackets
        bracket_pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            # If it's an opening bracket, push to stack
            if char in bracket_pairs.values():
                stack.append(char)

            # If it's a closing bracket
            elif char in bracket_pairs:
                # Check if stack is empty or top doesn't match
                if not stack or stack[-1] != bracket_pairs[char]:
                    return False
                stack.pop()

            # If character is not a bracket, string is invalid
            else:
                return False

        # Valid if stack is empty (all brackets matched)
        return len(stack) == 0


sol=Solution()
print(sol.isValid('()[]{}'))