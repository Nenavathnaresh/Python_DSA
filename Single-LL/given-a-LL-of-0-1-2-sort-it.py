def segregate(head):
    count = [0,0,0]
    curr = head 

    while curr :
        count[curr.data] += 1 
        curr = curr.next 
    curr = head 
    for i in range(3):
        for _ in range(count[i]):
            curr.data = i 
            curr = curr.next 
    return head 