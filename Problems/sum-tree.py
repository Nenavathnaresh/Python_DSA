class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def isSumTree(root):
    def check_and_sum(node):
        if node is None:
            return True, 0
        if node.left is None and node.right is None:
            return True, node.data
        
        left_is_sum_tree, left_sum = check_and_sum(node.left)
        right_is_sum_tree, right_sum = check_and_sum(node.right)
        
        current_sum = left_sum + right_sum
        
        is_current_node_sum_tree = (left_is_sum_tree and
                                    right_is_sum_tree and
                                    node.data == current_sum)
        
        return is_current_node_sum_tree, current_sum + node.data
    
    is_sum_tree, _ = check_and_sum(root)
    return is_sum_tree

# Helper function to build tree from level-order input
def build_tree(nodes):
    if not nodes or nodes[0] == 'N':
        return None

    root = Node(int(nodes[0]))
    queue = [root]
    index = 1

    while queue and index < len(nodes):
        current = queue.pop(0)

        if index < len(nodes) and nodes[index] != 'N':
            current.left = Node(int(nodes[index]))
            queue.append(current.left)
        index += 1

        if index < len(nodes) and nodes[index] != 'N':
            current.right = Node(int(nodes[index]))
            queue.append(current.right)
        index += 1

    return root

# Example usage with provided test case
nodes = ["62", "16", "15", "N", "8", "4", "7", "N", "8", "4"]
root = build_tree(nodes)

print(isSumTree(root))  # Expected Output: 1


############################################# 2nd method ################################################

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isSumTree(root):
    # Helper function to check if a given tree is a Sum Tree
    def checkAndSum(node):
        # Base case: if node is None, return (True, 0)
        if node is None:
            return (True, 0)
        
        # Base case: if node is a leaf, it is a Sum Tree
        if node.left is None and node.right is None:
            return (True, node.value)

        # Recursive case: check left and right subtrees
        isLeftSumTree, leftSum = checkAndSum(node.left)
        isRightSumTree, rightSum = checkAndSum(node.right)
        
        # Check the current node value against the sum of left and right
        isCurrentSumTree = node.value == leftSum + rightSum
        
        # Current node is a Sum Tree if it satisfies the property and both subtrees are Sum Trees
        isCurrentTreeSum = isLeftSumTree and isRightSumTree and isCurrentSumTree
        
        # Return the status and total sum including the current node
        return (isCurrentTreeSum, node.value + leftSum + rightSum)
    
    # Check the root and return only the status
    isTreeSum, _ = checkAndSum(root)
    return isTreeSum

# Test case 1
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(2)
print(isSumTree(root1))  # Output: True

# Test case 2
root2 = TreeNode(10)
root2.left = TreeNode(20)
root2.right = TreeNode(30)
root2.left.left = TreeNode(10)
root2.left.right = TreeNode(10)
print(isSumTree(root2))  # Output: False

# Additional Test Case
root3 = TreeNode(26)
root3.left = TreeNode(10)
root3.right = TreeNode(3)
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(6)
root3.right.right = TreeNode(3)
print(isSumTree(root3))  # Output: True

