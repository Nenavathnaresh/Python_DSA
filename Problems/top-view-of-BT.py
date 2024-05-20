from collections import deque

# Define the Node class for the binary tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def topView(root):
    if not root:
        return []
    
    # This dictionary will store the topmost node at each horizontal distance
    top_view_map = {}
    # Use deque for BFS
    queue = deque([(root, 0)])  # Each element is a tuple (node, horizontal_distance)
    
    while queue:
        node, hd = queue.popleft()
        
        # If this horizontal distance is not already in the map, add the node's data
        if hd not in top_view_map:
            top_view_map[hd] = node.data
        
        # Add the left child to the queue with horizontal distance hd-1
        if node.left:
            queue.append((node.left, hd - 1))
        
        # Add the right child to the queue with horizontal distance hd + 1
        if node.right:
            queue.append((node.right, hd + 1))
    
    # Extract the values from the map in order of their keys (sorted by horizontal distance)
    top_view_keys = sorted(top_view_map.keys())
    return [top_view_map[key] for key in top_view_keys]

# Example usage:
# Construct the tree:
#        1
#     /     \
#    2       3
#   /  \    /   \
#  4    5  6   7
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(topView(root))  # Output: [4, 2, 1, 3, 7]
