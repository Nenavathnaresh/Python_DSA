class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

class Solution:
    def isIdentical(self, root1, root2):
        # Base case: If both nodes are None, they are identical
        if not root1 and not root2:
            return True
        
        # If one is None and the other is not, they are not identical
        if not root1 or not root2:
            return False
        
        # Check if the current nodes' data are the same and recurse for left and right subtrees
        return (root1.data == root2.data and
                self.isIdentical(root1.left, root2.left) and
                self.isIdentical(root1.right, root2.right))

# Example usage:
# Tree 1:
#      1
#     / \
#    2   3
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

# Tree 2:
#      1
#     / \
#    2   3
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

# Tree 3:
#      1
#     / \
#    3   2
root3 = Node(1)
root3.left = Node(3)
root3.right = Node(2)

sol = Solution()
print(sol.isIdentical(root1, root2))  # Output: True
print(sol.isIdentical(root1, root3))  # Output: False
