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
    def hasPathSum(self,root,targetSum):
        def has_sum(node,cur_sum):
            if not node:
                return False
            cur_sum=cur_sum+node.val
            if not node.left and not node.right:
                return cur_sum==targetSum
            return has_sum(node.left,cur_sum) or has_sum(node.right,cur_sum)
        return has_sum(root,0)


values = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22

root = build_tree_from_list(values)
sol = Solution()
