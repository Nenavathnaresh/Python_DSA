from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def diagonalSum(root):
    if not root:
        return []

    # Dictionary to store sums of each diagonal level
    diagonal_sums = defaultdict(int)
    
    # Queue to store nodes along with their diagonal level
    queue = deque([(root, 0)])

    while queue:
        node, d = queue.popleft()
        # Add the current node's value to its diagonal level sum
        diagonal_sums[d] += node.val
        
        # Left child goes to the next diagonal level
        if node.left:
            queue.append((node.left, d + 1))
        
        # Right child stays on the same diagonal level
        if node.right:
            queue.append((node.right, d))
    
    # Extracting sums in order of their diagonal levels
    result = []
    for i in sorted(diagonal_sums.keys()):
        result.append(diagonal_sums[i])
    
    return result

# Example Usage:
# Construct the example tree:
#     4
#   /   \
#  1     3
#       /
#      3
root1 = TreeNode(4)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
root1.right.left = TreeNode(3)

print(diagonalSum(root1))  # Output: [7, 4]

# Construct another example tree:
#       10
#     /    \
#    8      2
#   / \    /
#  3   5  2
root2 = TreeNode(10)
root2.left = TreeNode(8)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(2)

print(diagonalSum(root2))  # Output: [12, 15, 3]
