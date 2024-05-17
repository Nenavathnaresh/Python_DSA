class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirror(node):
    if node is None:
        return
    
    # Recursively call mirror on left and right subtrees
    mirror(node.left)
    mirror(node.right)
    
    # Swap the left and right children
    node.left, node.right = node.right, node.left

def inorder_traversal(node, result):
    if node is None:
        return
    
    inorder_traversal(node.left, result)
    result.append(node.data)
    inorder_traversal(node.right, result)

# Example usage:

# Constructing the tree for Example 1:
#       1
#     /  \
#    2    3
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

# Constructing the tree for Example 2:
#       10
#      /  \
#     20   30
#    /  \
#   40  60
root2 = Node(10)
root2.left = Node(20)
root2.right = Node(30)
root2.left.left = Node(40)
root2.left.right = Node(60)

# Convert to mirror and get inorder traversal for root1
mirror(root1)
result1 = []
inorder_traversal(root1, result1)
print(result1)  # Output: [3, 1, 2]

# Convert to mirror and get inorder traversal for root2
mirror(root2)
result2 = []
inorder_traversal(root2, result2)
print(result2)  # Output: [30, 10, 60, 20, 40]
