class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate(head, k):
    if not head or k == 0:
        return head

    # Step 1: Determine the length of the list
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    # Step 2: If k is equal to the length of the list, no rotation is needed
    if k == length:
        return head

    # Step 3: Find the k-th node
    current = head
    for _ in range(k - 1):
        current = current.next

    # Step 4: Update pointers
    new_head = current.next
    current.next = None

    # Find the end of the rotated list and link it to the old head
    end = new_head
    while end.next:
        end = end.next
    end.next = head

    return new_head

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
head1 = createLinkedList([2, 4, 7, 8, 9])
k1 = 3
rotated_head1 = rotate(head1, k1)
printLinkedList(rotated_head1)  # Output: 8 9 2 4 7

# Test Case 2
head2 = createLinkedList([1, 2, 3, 4, 5, 6, 7, 8])
k2 = 4
rotated_head2 = rotate(head2, k2)
printLinkedList(rotated_head2)  # Output: 5 6 7 8 1 2 3 4
