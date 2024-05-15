class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

class Solution:
    def height(self, root):
        # Base case: If the tree is empty, return 0
        if root is None:
            return 0
        
        # Recursively find the height of left and right subtrees
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        # Height of the current node will be max of left_height and right_height + 1
        return 1 + max(left_height, right_height)

# Example usage:
# Constructing the tree:
#      1
#     / \
#    2   3
# Example 1:
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

# Constructing the tree:
#    2
#     \
#      1
#     /
#    3
# Example 2:
root2 = Node(2)
root2.right = Node(1)
root2.right.left = Node(3)

sol = Solution()
print(sol.height(root1))  # Output: 2
print(sol.height(root2))  # Output: 3
