class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def LCA(root, n1, n2):
    # Base case
    if root is None:
        return None
    
    # If both n1 and n2 are smaller than root, then LCA lies in left subtree
    if n1 < root.data and n2 < root.data:
        return LCA(root.left, n1, n2)
    
    # If both n1 and n2 are greater than root, then LCA lies in right subtree
    if n1 > root.data and n2 > root.data:
        return LCA(root.right, n1, n2)
    
    # If one of n1 or n2 is equal to root or n1 is on one side and n2 is on the other
    return root

# Example usage:

# Constructing the tree for Example 1:
#              5
#            /   \
#          4      6
#         /        \
#        3          7
#                    \
#                     8
root1 = Node(5)
root1.left = Node(4)
root1.right = Node(6)
root1.left.left = Node(3)
root1.right.right = Node(7)
root1.right.right.right = Node(8)

n1, n2 = 7, 8
lca_node = LCA(root1, n1, n2)
print(lca_node.data)  # Output: 7

# Constructing the tree for Example 2:
#      2
#    /   \
#   1     3
root2 = Node(2)
root2.left = Node(1)
root2.right = Node(3)

n1, n2 = 1, 3
lca_node = LCA(root2, n1, n2)
print(lca_node.data)  # Output: 2
