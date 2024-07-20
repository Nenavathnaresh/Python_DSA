class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def removeHalfNodes(root):
    if root is None:
        return None
    
    # Recursively remove half nodes from the left and right subtree
    root.left = removeHalfNodes(root.left)
    root.right = removeHalfNodes(root.right)
    
    # Check if the current node is a half-node
    if root.left is None and root.right is not None:
        return root.right
    if root.right is None and root.left is not None:
        return root.left
    
    # If not a half-node, return the current node
    return root

def inorderTraversal(root, result):
    if root is None:
        return
    inorderTraversal(root.left, result)
    result.append(root.value)
    inorderTraversal(root.right, result)

# Utility function to print inorder traversal of the tree
def printInorder(root):
    result = []
    inorderTraversal(root, result)
    print(' '.join(map(str, result)))

# Example Usage:
# Construct the tree for testing
# Input Tree: 5 -> [7, 8], 7 -> [2, None], 8 -> [None, None], 2 -> [None, None]
root = TreeNode(5)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)

# Remove half-nodes and print inorder traversal of modified tree
modified_root = removeHalfNodes(root)
printInorder(modified_root)  # Output should be: 2 5 8
