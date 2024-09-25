class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    if head is None or head.next is None:
        return True
    
    # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    second_half = reverseLinkedList(slow)

    # Step 3: Compare the two halves
    first_half = head
    is_palindrome = True
    temp_second_half = second_half  # Use this to restore the list later if needed
    while second_half:
        if first_half.data != second_half.data:
            is_palindrome = False
            break
        first_half = first_half.next
        second_half = second_half.next

    # Step 4: Restore the second half of the list (optional)
    reverseLinkedList(temp_second_half)

    return is_palindrome

# Helper function to reverse a linked list
def reverseLinkedList(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example usage:
# Creating a palindrome linked list: 1 -> 2 -> 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(1)

print(isPalindrome(head))  # Output: True

# Creating a non-palindrome linked list: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print(isPalindrome(head))  # Output: False
