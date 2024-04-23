def compute(head):

    curr = head 
    prev = None 

    while curr:
        nextNode = curr.next 
        curr.next = prev 
        prev = curr 
        curr = nextNode 
    head = prev 

    curr = head 
    maxNode = head 
    temp = None 

    while curr and curr.next :
        if curr.next.data < maxNode.data :
            temp = curr.next 
            curr.next = temp.next 
        else:
            curr = curr.next 
            maxNode = curr 

    curr = head 
    prev = None 
    while curr :
        nextNode = curr.next 
        curr.next = prev 
        prev = curr 
        curr = nextNode
    head = prev 
    return head 
