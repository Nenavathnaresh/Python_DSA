class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBST(root):
    def isBSTHelper(node, low, high):
        # Base case: If the node is None, it's a valid BST
        if not node:
            return True
        
        # Check the current node's value
        if node.val <= low or node.val >= high:
            return False
        
        # Recursively check the left and right subtrees with updated bounds
        return (isBSTHelper(node.left, low, node.val) and
                isBSTHelper(node.right, node.val, high))
    
    # Start with the entire range of valid integer values
    return isBSTHelper(root, float('-inf'), float('inf'))

# Example usage:

# Tree 1
#     2
#    / \
#   1   3
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

print(isBST(root1))  # Output: True

# Tree 2
#     2
#      \
#       7
#        \
#         6
#          \
#           9
root2 = TreeNode(2)
root2.right = TreeNode(7)
root2.right.right = TreeNode(6)
root2.right.right.right = TreeNode(9)

print(isBST(root2))  # Output: False

# Tree 3
#     10
#    /  \
#   5   20
#      /  \
#     9   25
root3 = TreeNode(10)
root3.left = TreeNode(5)
root3.right = TreeNode(20)
root3.right.left = TreeNode(9)
root3.right.right = TreeNode(25)

print(isBST(root3))  # Output: False
