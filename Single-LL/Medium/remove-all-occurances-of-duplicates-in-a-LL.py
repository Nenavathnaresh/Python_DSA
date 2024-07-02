class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    # Dummy node
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head

    while current:
        # Check for duplicates
        has_duplicates = False
        while current.next and current.val == current.next.val:
            current = current.next
            has_duplicates = True
        
        if has_duplicates:
            # Skip all duplicates
            prev.next = current.next
        else:
            # Move prev pointer to the next unique element
            prev = prev.next
        
        # Move current pointer
        current = current.next
    
    return dummy.next

# Helper function to create a linked list from a list
def createLinkedList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()

# Example usage:
# Test Case 1
head1 = createLinkedList([23, 28, 28, 35, 49, 49, 53, 53])
new_head1 = deleteDuplicates(head1)
printLinkedList(new_head1)  # Output: 23 35

# Test Case 2
head2 = createLinkedList([11, 11, 11, 11, 75, 75])
new_head2 = deleteDuplicates(head2)
printLinkedList(new_head2)  # Output: (Empty list)
