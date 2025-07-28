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
    def isSameTree(self,t1,t2):
        if t1 is None and t2 is None:
            return True
        if not t1 or not t2 or t1.val!=t2.val:
            return False
        return  self.isSameTree(t1.left,t2.left) and self.isSameTree(t1.right,t2.right)
values1=[1,2,1]
values2=[1,1,2]
t1=build_tree_from_list(values1)
t2=build_tree_from_list(values2)
sol=Solution()
sol.isSameTree(t1,t2)