class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sumNumbersFromRootToLeaf(root):
    def dfs(node, current_sum):
        if not node:
            return 0
        
        # Update the path sum for the current node
        current_sum = current_sum * 10 + node.value
        
        # If it's a leaf node, return the current path sum
        if not node.left and not node.right:
            return current_sum
        
        # Recursively compute sums for the left and right subtrees
        left_sum = dfs(node.left, current_sum)
        right_sum = dfs(node.right, current_sum)
        
        return left_sum + right_sum
    
    # Start DFS from the root with an initial path sum of 0
    return dfs(root, 0)
