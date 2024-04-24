def mulTwoList(head1, head2):
    M = 10**9+7
    L1 = ""
    L2 = ""
    curr = head1
    current = head2

    while curr :
        L1 += str(curr.data)
        curr = current.next 
    while current:
        L2 += str(current.data)
        current = current.next 
    res = (int(L1) * int(L2)) % M 
    return res 

# %%%%%%%%%%%%%%%%%%%%%%%%%% Method 2 %%%%%%%%%%%%%%%%%%%%%%

def mul(head1, head2):
    num1 , num2 = 0 
    M = 10**9+7

    while head1 or head2 :
        if head1:
            num1 = (num1 * 10 + head1.data) % M 
            head1 = head1.next 
        if head2 :
            num2 = (num2*10 + head2.data) % M 
            head2 = head2.next 
    res = (num1 * num2) % M
    return res 
                
                
                
