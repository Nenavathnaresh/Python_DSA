class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getMiddle(head):
    if not head:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data

# Example usage:
# Create a linked list
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)

print(getMiddle(head1))  # Output: 3

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(7)
head2.next.next.next.next = Node(5)
head2.next.next.next.next.next = Node(1)

print(getMiddle(head2))  # Output: 7
