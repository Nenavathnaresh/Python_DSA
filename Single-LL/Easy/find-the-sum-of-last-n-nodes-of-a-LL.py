class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        l = 0 
        curr = head
        
        while curr:
            l += 1 
            curr = curr.next 
        curr = head 
        curr_len = 0
        s = 0 
        while curr:
            curr_len += 1 
            if curr_len > l-n :
                s += curr.data 
            curr = curr.next 
        return s
    
############################################################################################

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def sum_of_last_n_nodes(head: ListNode, n: int) -> int:
    # Step 1: Initialize two pointers, both starting at head
    first = head
    second = head
    
    # Step 2: Move the first pointer n steps ahead
    for _ in range(n):
        first = first.next
    
    # Step 3: Move both pointers together until the first pointer reaches the end
    while first is not None:
        first = first.next
        second = second.next
    
    # Step 4: Sum the last n nodes starting from the second pointer
    total_sum = 0
    while second is not None:
        total_sum += second.data
        second = second.next
    
    return total_sum
