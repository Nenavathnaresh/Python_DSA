class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def countSubtreesWithSumX(root, X):
    # Initialize count of subtrees
    count = [0]  # Using a list to allow modification within nested function

    def subtree_sum(node):
        if not node:
            return 0
        
        # Calculate the sum of the left and right subtrees
        left_sum = subtree_sum(node.left)
        right_sum = subtree_sum(node.right)
        
        # Sum of the current subtree rooted at `node`
        total_sum = node.data + left_sum + right_sum
        
        # If the sum of the current subtree equals X, increment the count
        if total_sum == X:
            count[0] += 1
        
        return total_sum
    
    # Calculate the subtree sums starting from the root
    subtree_sum(root)
    
    # Return the count of subtrees with sum equal to X
    return count[0]

# Example usage:
# Construct the binary tree shown in the problem statement
root = Node(5)
root.left = Node(-10)
root.right = Node(3)
root.left.left = Node(9)
root.left.right = Node(8)
root.right.left = Node(-4)
root.right.right = Node(7)

# X value to check for
X = 7

# Get the count of subtrees with sum equal to X
result = countSubtreesWithSumX(root, X)
print(result)  # Output should be 2
