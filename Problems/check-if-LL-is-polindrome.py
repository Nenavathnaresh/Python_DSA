def Polindrome(head):
    if not head:
        return 
    res = []
    curr = head 
    while curr:
        res.append(curr.data)
        curr = curr.next 
    return res == res[::-1]

# %%%%%%%%%%%%%%%%%%%%%%%%%%%% 2nd method %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True
    
    # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Step 3: Compare the two halves
    left, right = head, prev
    while right:  # Compare till the end of the second half
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    
    # Optional Step 4: Restore the list (if needed)
    # Not necessary for the problem requirement
    # Reversing the second half again to restore the list can be done here

    return True

# Example usage:
# Constructing the linked list 1 -> 2 -> 1
node3 = ListNode(1)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

print(isPalindrome(head))  # Output: True (1)
