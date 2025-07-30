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
    def maxDepth(self,node):
        if node is None:
            return 0

        return 1+max(self.maxDepth(node.left),self.maxDepth(node.right))
values=[3,9,20,None,None,15,7]
root=build_tree_from_list(values)
sol=Solution()
sol.maxDepth(root)
