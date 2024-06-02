class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None

def get_length(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

def intersectPoint(head1, head2):
    if not head1 or not head2:
        return -1
    
    # Calculate the lengths of both linked lists
    len1 = get_length(head1)
    len2 = get_length(head2)
    
    # Determine the difference in lengths
    if len1 > len2:
        long_list = head1
        short_list = head2
        diff = len1 - len2
    else:
        long_list = head2
        short_list = head1
        diff = len2 - len1
    
    # Advance the pointer in the longer list by the difference in lengths
    for _ in range(diff):
        long_list = long_list.next
    
    # Traverse both lists together until a common node is found
    while long_list and short_list:
        if long_list == short_list:
            return long_list.data
        long_list = long_list.next
        short_list = short_list.next
    
    return -1

# Example usage:
# Creating intersection lists manually
# List 1: 3 -> 6 -> 9
#                    \
#                     15 -> 30 -> None
#                    /
# List 2:     10 ->

# Nodes
common = ListNode(15)
common.next = ListNode(30)

head1 = ListNode(3)
head1.next = ListNode(6)
head1.next.next = ListNode(9)
head1.next.next.next = common

head2 = ListNode(10)
head2.next = common

print(intersectPoint(head1, head2))  # Output: 15
