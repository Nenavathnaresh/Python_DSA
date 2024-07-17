class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def createTree(parent):
    n = len(parent)
    # Step 1: Create a node for each index
    nodes = [Node(i) for i in range(n)]
    
    # Step 2: Identify the root node
    root = None
    for i in range(n):
        if parent[i] == -1:
            root = nodes[i]
        else:
            # Step 3: Link the nodes
            if nodes[parent[i]].left is None:
                nodes[parent[i]].left = nodes[i]
            else:
                nodes[parent[i]].right = nodes[i]
    
    return root

# Function to print the level order traversal of the tree for verification
from collections import deque

def printLevelOrder(root):
    if not root:
        return
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(' '.join(map(str, result)))

# Example usage:
parent1 = [-1, 0, 0, 1, 1, 3, 5]
root1 = createTree(parent1)
printLevelOrder(root1)  # Output: 0 1 2 3 4 5 6

parent2 = [2, 0, -1]
root2 = createTree(parent2)
printLevelOrder(root2)  # Output: 2 0 1
