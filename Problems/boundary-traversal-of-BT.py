class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def is_leaf(node):
    return node.left is None and node.right is None

def add_left_boundary(node, boundary):
    curr = node.left
    while curr:
        if not is_leaf(curr):
            boundary.append(curr.data)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

def add_right_boundary(node, boundary):
    curr = node.right
    temp = []
    while curr:
        if not is_leaf(curr):
            temp.append(curr.data)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    # Reverse the collected right boundary nodes before adding
    while temp:
        boundary.append(temp.pop())

def add_leaves(node, boundary):
    if node is None:
        return
    if is_leaf(node):
        boundary.append(node.data)
    if node.left:
        add_leaves(node.left, boundary)
    if node.right:
        add_leaves(node.right, boundary)

def boundary(root):
    if not root:
        return []
    
    boundary = []
    
    if not is_leaf(root):
        boundary.append(root.data)
    
    add_left_boundary(root, boundary)
    add_leaves(root, boundary)
    add_right_boundary(root, boundary)
    
    return boundary

# Example Usage:
# Constructing the tree from the example:
#         1 
#       /   \
#      2     3  
#     / \   / \ 
#    4   5 6   7
#       / \
#      8   9

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.left.right.right = Node(9)

# Function call
print(boundary(root))  # Output should be [1, 2, 4, 8, 9, 6, 7, 3]
