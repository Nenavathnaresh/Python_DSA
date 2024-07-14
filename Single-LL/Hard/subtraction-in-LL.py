class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeLeadingZeros(head):
    while head is not None and head.val == 0:
        head = head.next
    return head if head else ListNode(0)  # To ensure we return at least one node.

def compareLists(l1, l2):
    # Remove leading zeros
    l1 = removeLeadingZeros(l1)
    l2 = removeLeadingZeros(l2)
    
    # Get lengths of both lists
    len1, len2 = 0, 0
    temp1, temp2 = l1, l2
    while temp1:
        len1 += 1
        temp1 = temp1.next
    while temp2:
        len2 += 1
        temp2 = temp2.next
    
    # If lengths are different, the longer list is larger
    if len1 > len2:
        return 1
    if len1 < len2:
        return -1
    
    # If lengths are the same, compare digit by digit
    while l1 and l2:
        if l1.val > l2.val:
            return 1
        if l1.val < l2.val:
            return -1
        l1 = l1.next
        l2 = l2.next
    
    # If all digits are the same, the numbers are equal
    return 0

def reverseList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def subtractLinkedLists(l1, l2):
    # Assumes l1 represents the larger number
    l1 = reverseList(l1)
    l2 = reverseList(l2)
    
    head = None
    temp = None
    borrow = 0
    
    while l1:
        sub = l1.val - (l2.val if l2 else 0) - borrow
        if sub < 0:
            sub += 10
            borrow = 1
        else:
            borrow = 0
        
        new_node = ListNode(sub)
        if head is None:
            head = new_node
        else:
            temp.next = new_node
        temp = new_node
        
        l1 = l1.next
        if l2:
            l2 = l2.next
    
    result = reverseList(head)
    return removeLeadingZeros(result)

def subLinkedList(l1, l2):
    comparison = compareLists(l1, l2)
    if comparison == 0:
        return ListNode(0)  # If both numbers are the same, return 0
    elif comparison > 0:
        return subtractLinkedLists(l1, l2)
    else:
        return subtractLinkedLists(l2, l1)

# Utility function to print linked list (for testing)
def printLinkedList(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")

# Example usage (for testing)
l1 = ListNode(1, ListNode(0, ListNode(0)))
l2 = ListNode(1, ListNode(2))
result = subLinkedList(l1, l2)
printLinkedList(result)  # Expected output: 8->8->None
