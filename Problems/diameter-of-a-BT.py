class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def diameter_of_tree(root):
    # Initialize the diameter
    diameter = [0]

    def height(node):
        if node is None:
            return 0

        # Get the height of the left and right subtrees
        left_height = height(node.left)
        right_height = height(node.right)

        # Update the diameter if the current path is larger
        diameter[0] = max(diameter[0], left_height + right_height + 1)

        # Return the height of the current node
        return 1 + max(left_height, right_height)

    # Start the height calculation and update the diameter
    height(root)

    # Since the diameter is the number of nodes on the longest path,
    # and the required answer is in terms of number of edges, we return diameter[0] - 1
    return diameter[0] - 1

# Example usage:
# Example 1:
#       1
#     /  \
#    2    3
# The diameter is 3 (nodes 2 -> 1 -> 3).
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
print(diameter_of_tree(root1))  # Output: 2

# Example 2:
#         10
#        /   \
#      20    30
#    /   \ 
#   40   60
# The diameter is 4 (nodes 40 -> 20 -> 10 -> 30).
root2 = Node(10)
root2.left = Node(20)
root2.right = Node(30)
root2.left.left = Node(40)
root2.left.right = Node(60)
print(diameter_of_tree(root2))  # Output: 3
