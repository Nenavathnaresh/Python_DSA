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
