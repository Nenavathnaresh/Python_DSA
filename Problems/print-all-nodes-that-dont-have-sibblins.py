class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def noSibling(root):
    # Helper function to perform DFS and collect nodes without siblings
    def dfs(node):
        if not node:
            return
        
        # Check if the node has only one child
        if node.left and not node.right:
            result.append(node.left.data)
        elif not node.left and node.right:
            result.append(node.right.data)
        
        # Recur for both left and right children
        dfs(node.left)
        dfs(node.right)
    
    result = []
    dfs(root)
    
    if not result:
        return [-1]
    
    return sorted(result)

# Example usage:

# Constructing the tree for Example 1:
#        37
#       /   
#     20
#     /     
#   113
root1 = Node(37)
root1.left = Node(20)
root1.left.left = Node(113)

# Constructing the tree for Example 2:
#        1
#       / \
#      2   3
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

print(noSibling(root1))  # Output: [20, 113]
print(noSibling(root2))  # Output: [-1]
