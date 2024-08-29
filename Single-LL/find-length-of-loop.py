def countNodesinLoop(head):
    slow = head 
    fast = head 

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 

        if slow == fast:
            count = 1 
            slow = slow.next 

            if slow != fast:
                slow = slow.next 
                count += 1 
            return count 
    return 0

#####################################################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_nodes_in_loop(head):
    slow = head
    fast = head
    
    # Step 1: Detect Loop using Floyd's Cycle-Finding Algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Loop detected
            break
    else:
        # No loop found
        return 0
    
    # Step 2: Find the start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    # Step 3: Count the number of nodes in the loop
    count = 1
    fast = fast.next
    while slow != fast:
        count += 1
        fast = fast.next
    
    return count

# Helper function to create a linked list with a loop
def create_linked_list_with_loop(arr, c):
    head = Node(arr[0])
    curr = head
    loop_start = None
    
    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
        if i == c:
            loop_start = curr
    
    if c != 0:
        curr.next = loop_start
    
    return head

# Example 1:
arr1 = [25, 14, 19, 33, 10, 21, 39, 90, 58, 45]
c1 = 4
head1 = create_linked_list_with_loop(arr1, c1)
print(count_nodes_in_loop(head1))  # Output: 7

# Example 2:
arr2 = [5, 4]
c2 = 0
head2 = create_linked_list_with_loop(arr2, c2)
print(count_nodes_in_loop(head2))  # Output: 0
