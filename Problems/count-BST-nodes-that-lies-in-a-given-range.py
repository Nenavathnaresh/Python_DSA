class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def getCountOfNode(root, l, h):
    # Base case: If the node is null, return 0
    if root is None:
        return 0

    # If the current node's value is within the range, include it
    if l <= root.data <= h:
        return (1 +
                getCountOfNode(root.left, l, h) +  # Count in the left subtree
                getCountOfNode(root.right, l, h))  # Count in the right subtree
    
    # If the current node's value is less than l, then we should search the right subtree
    elif root.data < l:
        return getCountOfNode(root.right, l, h)
    
    # If the current node's value is greater than h, then we should search the left subtree
    else:
        return getCountOfNode(root.left, l, h)

# Example usage
# Constructing the tree
#       10
#      /  \
#     5    50
#    /    /  \
#   1    40  100
root = Node(10)
root.left = Node(5)
root.right = Node(50)
root.left.left = Node(1)
root.right.left = Node(40)
root.right.right = Node(100)

l, h = 5, 45
print(getCountOfNode(root, l, h))  # Output: 3

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class Solution:
    def getCount(self,root,low,high):
        ##Your code here
        def inOrder(root,result):
            if not root:
                return None
            inOrder(root.left,result)
            result.append(root.data)
            inOrder(root.right,result)
        result = []
        
        inOrder(root,result)
        count = 0
        for i in range(len(result)):
            if result[i] >= low and result[i] <= high:
                count += 1 
        return count