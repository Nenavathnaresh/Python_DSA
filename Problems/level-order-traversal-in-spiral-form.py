from collections import deque

class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

class Solution:
    def findSpiral(self, root):
        if not root:
            return []
        
        result = []
        deque_nodes = deque([root])
        left_to_right = False
        
        while deque_nodes:
            level_size = len(deque_nodes)
            level_nodes = []
            
            for _ in range(level_size):
                if left_to_right:
                    node = deque_nodes.popleft()
                    level_nodes.append(node.data)
                    if node.left:
                        deque_nodes.append(node.left)
                    if node.right:
                        deque_nodes.append(node.right)
                else:
                    node = deque_nodes.pop()
                    level_nodes.append(node.data)
                    if node.right:
                        deque_nodes.appendleft(node.right)
                    if node.left:
                        deque_nodes.appendleft(node.left)
            
            result.extend(level_nodes)
            left_to_right = not left_to_right
        
        return result

# Example usage:
# Construct the tree:
#      1
#    /   \
#   3     2
root1 = Node(1)
root1.left = Node(3)
root1.right = Node(2)

# Tree for second example:
#           10
#         /     \
#        20     30
#      /    \
#    40     60
root2 = Node(10)
root2.left = Node(20)
root2.right = Node(30)
root2.left.left = Node(40)
root2.left.right = Node(60)

sol = Solution()
print(sol.findSpiral(root1))  # Output: [1, 3, 2]
print(sol.findSpiral(root2))  # Output: [10, 20, 30, 60, 40]
