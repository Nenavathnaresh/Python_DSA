class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leftView(root):
    if not root:
        return []

    left_view = []
    queue = [root]

    while queue:
        # Record the first node in the current level
        left_view.append(queue[0].val)

        # Update the queue for the next level
        next_level = []
        for node in queue:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        queue = next_level

    return left_view

# Test case
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.right = TreeNode(8)

print(leftView(root))  # Output: [1, 2, 4, 8]

#####################################################################################

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leftView(root):
    if not root:
        return []

    queue = deque([(root, 0)])  # Queue stores nodes along with their level
    left_view = []
    max_level_seen = -1
    
    while queue:
        node, level = queue.popleft()
        
        # If this is the first node at this level, add it to the left view
        if level > max_level_seen:
            left_view.append(node.val)
            max_level_seen = level
        
        # Enqueue left child first, then right child
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return left_view

# Example usage:
# Constructing the tree
#          1
#       /     \
#     2        3
#   /     \    /    \
#  4     5   6    7
#   \
#     8   
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.right = TreeNode(8)

print(leftView(root))  # Output: [1, 2, 4, 8]

