class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def sortedArrayToBST(self, num: list[int]):
        if not num:
            return None
        mid = len(num) // 2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])
        return root
