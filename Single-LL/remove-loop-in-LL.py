class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def removeLoop(head):
    if not head or not head.next:
        return  # No loop possible if the list is empty or has only one node

    slow = head
    fast = head

    # Detecting loop using Floyd’s Cycle-Finding Algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break  # Loop detected

    if slow != fast:
        return  # No loop found

    # Finding the start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Removing the loop
    start_of_loop = slow
    while fast.next != start_of_loop:
        fast = fast.next
    fast.next = None

# Helper function to create a linked list from an array and create a loop at position X
def createLinkedList(values, X):
    if len(values) == 0:
        return None

    head = ListNode(values[0])
    current = head
    loopNode = None

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == X - 1:
            loopNode = current

    if X > 0:
        current.next = loopNode

    return head

# Helper function to print the linked list (for verification)
def printList(head):
    visited = set()
    current = head
    while current:
        if current in visited:
            print("->", current.value, "(loop starts here)", end=" ")
            break
        visited.add(current)
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage:
values = [1, 3, 4]
X = 2  # Creating a loop at position 2
head = createLinkedList(values, X)
print("Before removing the loop:")
printList(head)
removeLoop(head)
print("After removing the loop:")
printList(head)

values = [1, 8, 3, 4]
X = 0  # No loop
head = createLinkedList(values, X)
print("Before removing the loop:")
printList(head)
removeLoop(head)
print("After removing the loop:")
printList(head)

values = [1, 2, 3, 4]
X = 1  # Creating a loop at position 1
head = createLinkedList(values, X)
print("Before removing the loop:")
printList(head)
removeLoop(head)
print("After removing the loop:")
printList(head)
