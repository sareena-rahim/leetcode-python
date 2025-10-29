from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


class Solution:


    def build_tree_from_lst(self,values):
        if not values or values[0] is None:
            return None
        root=TreeNode(values[0])
        queue=deque([root])
        i=1

        while queue and i <len(values):
            current=queue.popleft()

            if i <len(values) and values[i] is not None:
                current.left=TreeNode(values[i])
                queue.append(current.left)
            i=i+1
            if i<len(values) and values[i] is not None:
                current.right=TreeNode(values[i])
                queue.append(current.right)
            i=i+1
        return root

    def isBalanced(self, root):

        def height(root):
            if not root:
                return 0
            left_height=height(root.left)
            if left_height==-1:
                return -1

            right_height=height(root.right)
            if right_height==-1:
                return -1

            if abs(left_height-right_height)>1:
                return -1
            return max(left_height,right_height)+1
        return height(root)!=-1

sol=Solution()
values=[3,9,20,None,None,15,7]
root=sol.build_tree_from_lst(values)
result=sol.isBalanced(root)