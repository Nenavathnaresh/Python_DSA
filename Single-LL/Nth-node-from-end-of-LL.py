def getNthfromLast(head,n):
    if not head:
        return -1
    firstPtr = head
    secondPtr = head 
    
    for _ in range(n):
        if not secondPtr:
            return -1
        secondPtr = secondPtr.next 
    while secondPtr:
        firstPtr = firstPtr.nex
        secondPtr = secondPtr.next 
    return firstPtr.data 
