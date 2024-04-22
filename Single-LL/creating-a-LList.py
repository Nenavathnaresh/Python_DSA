class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Example usage:
# Create a linked list
llist = LinkedList()

# Append nodes to the linked list
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

# Print the linked list
llist.print_list()  # Output: 1 2 3 4 5
