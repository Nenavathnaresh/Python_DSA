class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def hasPathSum(node, s):
    # If the node is None, return False
    if not node:
        return False
    
    # Check if we are at a leaf node
    if not node.left and not node.right:
        return s == node.data
    
    # Otherwise, check the left and right subtrees
    s -= node.data
    return hasPathSum(node.left, s) or hasPathSum(node.right, s)

# Example usage:

# Example 1:
# Tree:
#            1
#          /   \
#        2      3
# s = 2
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
print(hasPathSum(root1, 2))  # Output: False

# Example 2:
# Tree:
#            1
#          /   \
#        2      3
# s = 4
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
print(hasPathSum(root2, 4))  # Output: True
