class Node:
    def __init__(self, data, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random

def copyRandomList(head):
    if not head:
        return None

    # Step 1: Create new nodes alongside the original nodes
    curr = head
    while curr:
        new_node = Node(curr.data)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next
    
    # Step 2: Assign random pointers for the copied nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    
    # Step 3: Separate the original list and the copied list
    curr = head
    copy_head = head.next
    copy_curr = copy_head
    while curr:
        curr.next = curr.next.next
        if copy_curr.next:
            copy_curr.next = copy_curr.next.next
        curr = curr.next
        copy_curr = copy_curr.next
    
    return copy_head
