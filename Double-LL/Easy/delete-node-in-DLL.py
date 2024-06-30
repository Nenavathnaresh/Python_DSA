class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def deleteNode(head, x):
    if head is None:
        return None
    
    # If the head needs to be removed
    if x == 1:
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head
    
    # Traverse to the node to be deleted
    current = head
    for i in range(x - 1):
        current = current.next
        if current is None:
            return head
    
    # Update the pointers
    if current.next:
        current.next.prev = current.prev
    if current.prev:
        current.prev.next = current.next
    
    return head

# Function to print the list (for testing purposes)
def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Example usage:
# LinkedList = 1 <--> 3 <--> 4, x = 3
head = Node(1)
second = Node(3)
third = Node(4)
head.next = second
second.prev = head
second.next = third
third.prev = second

print("Original List:")
printList(head)
head = deleteNode(head, 3)
print("After Deleting position 3:")
printList(head)

# LinkedList = 1 <--> 5 <--> 2 <--> 9, x = 1
head = Node(1)
second = Node(5)
third = Node(2)
fourth = Node(9)
head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third

print("Original List:")
printList(head)
head = deleteNode(head, 1)
print("After Deleting position 1:")
printList(head)
