class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque

def Kdistance(root, k):
    if not root:
        return []
    
    queue = deque([(root, 0)])  # Queue of pairs (node, level)
    result = []
    
    while queue:
        node, level = queue.popleft()
        
        if level == k:
            result.append(node.data)
        
        # If the current level is greater than k, we can stop processing further levels
        if level > k:
            break
        
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return result

# Example usage:

# Example 1:
# k = 0
# Tree:
#       1
#     /   \
#    3     2
root1 = Node(1)
root1.left = Node(3)
root1.right = Node(2)
print(Kdistance(root1, 0))  # Output: [1]

# Example 2:
# k = 3
# Tree:
#         1
#        /
#       2
#        \
#         1
#       /  \
#      5    3
root2 = Node(1)
root2.left = Node(2)
root2.left.right = Node(1)
root2.left.right.left = Node(5)
root2.left.right.right = Node(3)
print(Kdistance(root2, 3))  # Output: [5, 3]
