class Node:
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Example usage
# Constructing the tree:
#          1
#       /     \
#     2        3
#   /    \     /   \
#  4     5   6    7
#    \
#     8

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.right = Node(8)

print(levelOrder(root))  # Output: [[1], [2, 3], [4, 5, 6, 7], [8]]
