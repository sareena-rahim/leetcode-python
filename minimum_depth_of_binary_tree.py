from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def build_tree_from_list(values):
    if not  values or values[0] is None:
        return None
    root=TreeNode(values[0])
    queue=deque([root])
    i=1
    while queue and i <len(values):
        current=queue.popleft()

        if i<len(values) and values[i] is not None:
            current.left=TreeNode(values[i])
            queue.append(current.left)

        i=i+1

        if i<len(values) and values[i] is not None:
            current.right=TreeNode(values[i])
            queue.append(current.right)
        i=i+1
    return root
class Solution:
    def minDepth(self,node):
        if node is None:
            return 0
        if not node.left:
            return 1+self.minDepth(node.right)
        if not node.right:
            return 1+self.minDepth(node.left)
        return 1+min(self.minDepth(node.left),self.minDepth(node.right))
values=[2,None,3,None,4,None,5,None,6]
root=build_tree_from_list(values)
sol=Solution()