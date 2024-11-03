def isLengthEven(self, head):
        # Code here
    curr = head 
    length = 0  
    while curr:
        length += 1 
        curr = curr.next
    return True if length % 2 == 0 else False

#########################################################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isLengthEven(head):
    # Use a boolean flag to track even/odd length
    is_even = True
    current = head
    
    # Traverse through the linked list
    while current:
        is_even = not is_even
        current = current.next
    
    # If is_even is True, length is even; else, it's odd
    return is_even
