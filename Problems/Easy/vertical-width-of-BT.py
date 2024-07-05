# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def verticalWidth(root):
    if not root:
        return 0

    # Set to store unique horizontal distances
    hd_set = set()

    # Helper function to perform DFS and track horizontal distances
    def dfs(node, hd):
        if not node:
            return
        # Add the current horizontal distance to the set
        hd_set.add(hd)
        # Traverse the left subtree with horizontal distance decreased by 1
        dfs(node.left, hd - 1)
        # Traverse the right subtree with horizontal distance increased by 1
        dfs(node.right, hd + 1)

    # Start DFS with root node and horizontal distance 0
    dfs(root, 0)
    
    # The vertical width is the number of unique horizontal distances
    return len(hd_set)

# Example Usage:
# Construct the example tree:
#          1
#        /    \
#       2      3
#      / \    /  \
#     4   5  6   7
#             \   \
#              8   9
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
root1.right.left.right = TreeNode(8)
root1.right.right.right = TreeNode(9)

print(verticalWidth(root1))  # Output: 6

# Construct another example tree:
#      1
#     /  \
#    2    3
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(verticalWidth(root2))  # Output: 3
