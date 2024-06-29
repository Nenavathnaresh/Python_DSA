class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def are_identical(head1, head2):
    # Initialize two pointers for both linked lists
    current1 = head1
    current2 = head2
    
    # Traverse both lists and compare nodes
    while current1 is not None and current2 is not None:
        if current1.data != current2.data:
            return False
        current1 = current1.next
        current2 = current2.next
    
    # If both lists are of different lengths, they are not identical
    if current1 is not None or current2 is not None:
        return False
    
    return True

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example usage:
# LinkedList1: 1->2->3->4->5
# LinkedList2: 1->2->3->4->5
head1 = create_linked_list([1, 2, 3, 4, 5])
head2 = create_linked_list([1, 2, 3, 4, 5])
print(are_identical(head1, head2))  # Output: True

# LinkedList1: 1->2->3->4->5->6
# LinkedList2: 99->59->42->20
head1 = create_linked_list([1, 2, 3, 4, 5, 6])
head2 = create_linked_list([99, 59, 42, 20])
print(are_identical(head1, head2))  # Output: False
