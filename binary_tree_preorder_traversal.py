from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def build_tree_from_list(self, values):
        if not values or values[0] is None:
            return None
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            current = queue.popleft()

            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i = i + 1

            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i = i + 1

        return root

    def preorderTraversal(self, node, res=None):
        if res is None:
            res = []
        if node is None:
            return res

        res.append(node.val)

        self.preorderTraversal(node.left, res)
        self.preorderTraversal(node.right, res)

        return res


values = [1, None, 2, 3]
sol = Solution()
root = sol.build_tree_from_list(values)

final = sol.preorderTraversal(root)
print(final)