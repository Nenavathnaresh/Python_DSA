class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBSTUtil(node, min_val, max_val):
    # Base case: an empty tree is considered as a BST
    if node is None:
        return True
    
    # Check if current node's value is within the valid range
    if node.val <= min_val or node.val >= max_val:
        return False
    
    # Check recursively for left and right subtrees
    return (isBSTUtil(node.left, min_val, node.val) and
            isBSTUtil(node.right, node.val, max_val))

def isBST(root):
    # Call the utility function with initial min and max values
    return isBSTUtil(root, float('-inf'), float('inf'))

##################################################################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBST(root):
    stack = []
    prev_val = float('-inf')
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if current.val <= prev_val:
            return False
        prev_val = current.val
        current = current.right
    return True

################################################################################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBSTUtil(node, min_val, max_val):
    if node is None:
        return True
    if node.val < min_val or node.val > max_val:
        return False
    return (isBSTUtil(node.left, min_val, node.val - 1) and
            isBSTUtil(node.right, node.val + 1, max_val))

def isBST(root):
    return isBSTUtil(root, float('-inf'), float('inf'))


###################################################################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBST(root):
    if not root:
        return True
    stack = [(root, float('-inf'), float('inf'))]
    while stack:
        node, min_val, max_val = stack.pop()
        if not node:
            continue
        if node.val <= min_val or node.val >= max_val:
            return False
        stack.append((node.right, node.val, max_val))
        stack.append((node.left, min_val, node.val))
    return True

###############################################################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBST(root):
    current = root
    prev_val = float('-inf')
    while current:
        if not current.left:
            if current.val <= prev_val:
                return False
            prev_val = current.val
            current = current.right
        else:
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right
            if not pre.right:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                if current.val <= prev_val:
                    return False
                prev_val = current.val
                current = current.right
    return True


# Test cases
# Example 1
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(isBST(root1))  # Output: True

# Example 2
root2 = TreeNode(2)
root2.right = TreeNode(7)
root2.right.right = TreeNode(6)
root2.right.right.right = TreeNode(5)
root2.right.right.right.right = TreeNode(9)
root2.right.right.right.right.right = TreeNode(2)
root2.right.right.right.right.right.right = TreeNode(6)
print(isBST(root2))  # Output: False

#################################################

