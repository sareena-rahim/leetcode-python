from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def createTree(self,lst):
        if not lst or  lst[0] is None:
            return None
        root=TreeNode(lst[0])
        queue=deque([root])

        i=1
        while queue and i<len(lst):
            node=queue.popleft()

            if i<len(lst) and lst[i] is not None:
                node.left=TreeNode(lst[i])
                queue.append(node.left)
            i=i+1
            if i<len(lst) and lst[i] is not None:
                node.right=TreeNode(lst[i])
                queue.append(node.right)
            i=i+1
        return root

    def levelOrder(self,root: TreeNode):
        if not root:
            return []


        result = []
        queue=deque([root])
        while queue:
            level = []
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result


lst = [1, 2, 3, None, 4, 5]
sol=Solution()
root = sol.createTree(lst)

# Call levelOrder
result = sol.levelOrder(root)


