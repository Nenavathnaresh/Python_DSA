from collections import deque, defaultdict

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def bottomView(root):
    if not root:
        return []

    # Queue for level order traversal
    queue = deque([(root, 0)])  # (node, horizontal distance)
    
    # Dictionary to store the bottom view (HD -> node.data)
    hd_node_map = {}
    
    while queue:
        node, hd = queue.popleft()
        
        # Update the node at each horizontal distance
        hd_node_map[hd] = node.data
        
        # Add the left child with HD - 1
        if node.left:
            queue.append((node.left, hd - 1))
        
        # Add the right child with HD + 1
        if node.right:
            queue.append((node.right, hd + 1))
    
    # Extract the values from the map, sorted by HD
    bottom_view = [hd_node_map[hd] for hd in sorted(hd_node_map)]
    return bottom_view

# Example usage:
# Creating the binary tree from the example
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print(bottomView(root))  # Output: [5, 10, 3, 14, 25]
