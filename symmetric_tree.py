from collections import deque

# Binary tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build binary tree from list (level-order)
def build_tree_from_list(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Assign left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Assign right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

# Function to check if tree is symmetric
def isSymmetric(root):
    if not root:
        return True

    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

    return is_mirror(root.left, root.right)

tree1 = build_tree_from_list([1,2,2,3,4,4,3])

print(isSymmetric(tree1))  # True

