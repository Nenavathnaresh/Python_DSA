class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque

def check(root):
    if not root:
        return True
    
    queue = deque([(root, 0)])  # Queue of pairs (node, level)
    leaf_level = None
    
    while queue:
        node, level = queue.popleft()
        
        # Check if it's a leaf node
        if not node.left and not node.right:
            if leaf_level is None:
                leaf_level = level  # Set the level of the first leaf node
            elif leaf_level != level:
                return False
        
        # Add children to the queue with incremented level
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return True

# Example usage:

# Example 1:
# Tree:
#     1
#    / \
#   2   3
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
print(check(root1))  # Output: True

# Example 2:
# Tree:
#     10
#    /  \
#   20   30
#  /  \
# 10   15
root2 = Node(10)
root2.left = Node(20)
root2.right = Node(30)
root2.left.left = Node(10)
root2.left.right = Node(15)
print(check(root2))  # Output: False
