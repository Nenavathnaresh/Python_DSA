class TreeNode:
    def __init__(self, data=0, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

def populate_next(root):
    # Helper function for reverse inorder traversal
    def reverse_inorder(node, prev):
        if not node:
            return prev
        # Traverse the right subtree first
        prev = reverse_inorder(node.right, prev)
        # Set the next pointer of the current node
        node.next = prev
        # Update the previously visited node to the current node
        prev = node
        # Traverse the left subtree
        return reverse_inorder(node.left, prev)
    
    # Start the reverse inorder traversal with an initial previous node as None
    reverse_inorder(root, None)

# Example usage:
# Constructing the binary tree:
#        10
#       /  \
#      8   12
#     /
#    3
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(3)

populate_next(root)

# Function to print the inorder traversal along with next pointers
def print_inorder_with_next(node):
    if node:
        print_inorder_with_next(node.left)
        next_data = node.next.data if node.next else -1
        print(f'{node.data}->{next_data}', end=' ')
        print_inorder_with_next(node.right)

print_inorder_with_next(root)
