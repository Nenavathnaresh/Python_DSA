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

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

MOD = 10**9 + 7

def multiplyTwoLists(L1, L2):
    # Helper function to compute the number represented by a linked list
    def getNumber(head):
        num = 0
        while head:
            num = (num * 10 + head.data) % MOD
            head = head.next
        return num
    
    # Get the number represented by both linked lists
    num1 = getNumber(L1)
    num2 = getNumber(L2)
    
    # Multiply the two numbers and return the result modulo 10^9 + 7
    return (num1 * num2) % MOD

# Example usage:
# Linked list 1: 3 -> 2 (represents 32)
L1 = Node(3)
L1.next = Node(2)

# Linked list 2: 2 (represents 2)
L2 = Node(2)

print(multiplyTwoLists(L1, L2))  # Output: 64

# Linked list 1: 1 -> 0 -> 0 (represents 100)
L1 = Node(1)
L1.next = Node(0)
L1.next.next = Node(0)

# Linked list 2: 1 -> 0 (represents 10)
L2 = Node(1)
L2.next = Node(0)

print(multiplyTwoLists(L1, L2))  # Output: 1000

                
                
                
