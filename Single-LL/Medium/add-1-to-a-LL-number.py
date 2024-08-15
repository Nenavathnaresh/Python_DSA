class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def addOne(head):
    # Step 1: Reverse the linked list
    head = reverse_list(head)
    
    # Step 2: Add 1 to the reversed list
    carry = 1
    current = head
    
    while current:
        current.data += carry
        if current.data == 10:
            current.data = 0
            carry = 1
        else:
            carry = 0
            break
        if not current.next and carry:
            current.next = Node(1)
            carry = 0
        current = current.next
    
    # Step 3: Reverse the list back to original order
    head = reverse_list(head)
    
    return head

def printList(head):
    while head:
        print(head.data, end="")
        head = head.next
    print()

# Example Usage
head = Node(4)
head.next = Node(5)
head.next.next = Node(6)

new_head = addOne(head)
printList(new_head)  # Output: 457
