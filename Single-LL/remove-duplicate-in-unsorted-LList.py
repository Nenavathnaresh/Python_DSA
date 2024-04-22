def removeDuplicate(head):
    if not head :
        return None 
    curr = head 
    seen = set()
    seen.add(curr.data)
    while curr.next :
        if curr.next.data in seen:
            curr.next = curr.next.next 
        else:
            seen.add(curr.next.data)
            curr = curr.next
    return head 