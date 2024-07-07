class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def findAncestors(root, target):
    # Helper function to find the ancestors
    def helper(node, target):
        if not node:
            return False
        if node.data == target:
            return True
        if helper(node.left, target) or helper(node.right, target):
            ancestors.append(node.data)
            return True
        return False
    
    ancestors = []
    helper(root, target)
    return ancestors

# Example usage:
# Creating the binary tree:
#         1
#       /   \
#      2     3
#    /  \   /  \
#   4   5  6   8
#  /
# 7
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(8)
root.left.left.left = Node(7)

target = 7
print(findAncestors(root, target))  # Output: [4, 2, 1]

target = 1
print(findAncestors(root, target))  # Output: []
