# Definition for a binary tree node.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def TreeToList(root):
    # Initialize 'prev' to None and 'head' to store the first node of DLL
    prev = None
    head = None
    
    def inorder_convert(node):
        nonlocal prev, head
        
        if not node:
            return
        
        # Traverse the left subtree first
        inorder_convert(node.left)
        
        # Now process the current node
        if prev is None:
            # If 'prev' is None, this is the first node (leftmost node)
            head = node
        else:
            # Link the current node with the previous node
            prev.right = node
            node.left = prev
        
        # Update 'prev' to current node
        prev = node
        
        # Traverse the right subtree
        inorder_convert(node.right)
    
    # Start the inorder conversion
    inorder_convert(root)
    
    # Return the head of the doubly linked list
    return head

# Utility function to print the DLL from the head node
def print_DLL(head):
    while head:
        print(head.data, end=" ")
        head = head.right
    print()

# Example usage:
# Creating the binary tree from the first example
root = Node(1)
root.left = Node(3)
root.right = Node(2)

# Converting the binary tree to a doubly linked list
dll_head = TreeToList(root)

# Printing the doubly linked list
print_DLL(dll_head)  # Output: 3 1 2

# Creating the binary tree from the second example
root2 = Node(10)
root2.left = Node(20)
root2.right = Node(30)
root2.left.left = Node(40)
root2.left.right = Node(60)

# Converting the binary tree to a doubly linked list
dll_head2 = TreeToList(root2)

# Printing the doubly linked list
print_DLL(dll_head2)  # Output: 40 20 60 10 30
