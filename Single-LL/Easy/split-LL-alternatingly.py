class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def alternatingSplitList(head):
    # Initialize the two resulting sublists and their tails
    list1_head = list1_tail = None
    list2_head = list2_tail = None
    
    # Use a pointer to traverse the original list
    current = head
    index = 0  # This will help in alternating the nodes
    
    while current is not None:
        # Clone the current node to avoid modifying the original list
        new_node = Node(current.data)
        
        if index % 2 == 0:  # Even index -> add to list1
            if list1_head is None:
                list1_head = new_node
                list1_tail = list1_head
            else:
                list1_tail.next = new_node
                list1_tail = list1_tail.next
        else:  # Odd index -> add to list2
            if list2_head is None:
                list2_head = new_node
                list2_tail = list2_head
            else:
                list2_tail.next = new_node
                list2_tail = list2_tail.next
        
        # Move to the next node in the original list
        current = current.next
        index += 1
    
    # Terminate both sublists
    if list1_tail:
        list1_tail.next = None
    if list2_tail:
        list2_tail.next = None
    
    # Return the heads of the two lists
    return [list1_head, list2_head]

# Helper function to print the linked list
def printList(head):
    result = []
    current = head
    while current is not None:
        result.append(str(current.data))
        current = current.next
    print("->".join(result))

# Example Usage
head = Node(0)
head.next = Node(1)
head.next.next = Node(0)
head.next.next.next = Node(1)
head.next.next.next.next = Node(0)
head.next.next.next.next.next = Node(1)

result = alternatingSplitList(head)
print("List 1:")
printList(result[0])
print("List 2:")
printList(result[1])
