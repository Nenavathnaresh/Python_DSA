class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def isMirror(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    return (left.data == right.data and 
            isMirror(left.left, right.right) and 
            isMirror(left.right, right.left))

def isSymmetric(root):
    if root is None:
        return True
    return isMirror(root.left, root.right)

# Example usage:

# Example 1:
#          5
#        /   \
#       1     1
#      /       \
#     2         2
root1 = Node(5)
root1.left = Node(1)
root1.right = Node(1)
root1.left.left = Node(2)
root1.right.right = Node(2)

print(isSymmetric(root1))  # Output: True

# Example 2:
#          5
#        /   \
#      10     10
#     /  \     \
#    20  20     30
root2 = Node(5)
root2.left = Node(10)
root2.right = Node(10)
root2.left.left = Node(20)
root2.left.right = Node(20)
root2.right.right = Node(30)

print(isSymmetric(root2))  # Output: False
