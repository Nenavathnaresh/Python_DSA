class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    stack = []
    
    while queue:
        node = queue.pop(0)
        stack.append(node)
        
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    
    while stack:
        node = stack.pop()
        result.append(node.val)
    
    return result

# Example usage:

# Example 1:
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
print(reverseLevelOrder(root1))  # Output: [3, 2, 1]

# Example 2:
root2 = TreeNode(10)
root2.left = TreeNode(20)
root2.right = TreeNode(30)
root2.left.left = TreeNode(40)
root2.left.right = TreeNode(60)
print(reverseLevelOrder(root2))  # Output: [40, 60, 20, 30, 10]
