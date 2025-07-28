from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def build_tree_from_list(values):
    if not values or values[0] is None:
        return None
    root=TreeNode(values[0])
    queue=deque([root])
    i=1
    while queue and i<len(values):
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
    def inorderTraversal(self,root):
        if root is None:
              return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)



values=[1,None,2,3]
root=build_tree_from_list(values)
sol=Solution()
sol.inorderTraversal(root)
