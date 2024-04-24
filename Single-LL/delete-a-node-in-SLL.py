def delNode(head,k):
    if head is None:
        return None 
    if k == 1:
        return head.next 
    curr = head 
    for i in range(k-2):
        if curr is None:
            return head 
        curr = curr.next 
    if curr is None or curr.next is None:
        return head 
    curr.next = curr.next.next 
    return head 