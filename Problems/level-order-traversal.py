from collections import deque

class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result

# Example usage:
# Constructing the tree for Example 1:
#     1
#   /   \ 
#  3     2
root1 = Node(1)
root1.left = Node(3)
root1.right = Node(2)

# Constructing the tree for Example 2:
#         10
#      /      \
#     20       30
#   /   \
#  40   60
root2 = Node(10)
root2.left = Node(20)
root2.right = Node(30)
root2.left.left = Node(40)
root2.left.right = Node(60)

sol = Solution()
print(sol.levelOrder(root1))  # Output: [1, 3, 2]
print(sol.levelOrder(root2))  # Output: [10, 20, 30, 40, 60]
