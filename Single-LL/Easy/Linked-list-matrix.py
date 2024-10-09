# Define the node for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

def construct_2d_linked_list(mat):
    if not mat or not mat[0]:
        return None
    
    n = len(mat)
    # Create a 2D array to store the linked list nodes
    nodes = [[None for _ in range(n)] for _ in range(n)]
    
    # Create the nodes and store them in the nodes array
    for i in range(n):
        for j in range(n):
            nodes[i][j] = Node(mat[i][j])
    
    # Link the nodes appropriately
    for i in range(n):
        for j in range(n):
            if j < n - 1:  # Link right
                nodes[i][j].right = nodes[i][j + 1]
            if i < n - 1:  # Link down
                nodes[i][j].down = nodes[i + 1][j]
    
    # Return the head of the 2D linked list (top-left corner node)
    return nodes[0][0]

# Function to print the 2D linked list
def print_2d_linked_list(head):
    down = head
    while down:
        right = down
        while right:
            print(right.data, end=" ")
            right = right.right
        print()
        down = down.down

# Example usage:
mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[23, 28], [23, 28]]

head1 = construct_2d_linked_list(mat1)
print("2D Linked List for mat1:")
print_2d_linked_list(head1)

head2 = construct_2d_linked_list(mat2)
print("2D Linked List for mat2:")
print_2d_linked_list(head2)
