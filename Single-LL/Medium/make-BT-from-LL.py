class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def constructBinaryTreeFromLinkedList(head):
    if not head:
        return None

    root = TreeNode(head.val)
    queue = deque([root])
    current = head.next

    while current:
        parent = queue.popleft()

        # Left child
        left_child = TreeNode(current.val)
        parent.left = left_child
        queue.append(left_child)
        current = current.next
        if not current:
            break

        # Right child
        right_child = TreeNode(current.val)
        parent.right = right_child
        queue.append(right_child)
        current = current.next

    return root

def levelOrderTraversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Helper function to print the linked list (for testing purposes)
def printLinkedList(head):
    while head:
        print(head.val, end="->" if head.next else "\n")
        head = head.next

# Helper function to create a linked list from a list of values (for testing purposes)
def createLinkedList(arr):
    dummy = ListNode()
    current = dummy
    for value in arr:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Example usage
n = 5
values = [1, 2, 3, 4, 5]
head = createLinkedList(values)

root = constructBinaryTreeFromLinkedList(head)
print(levelOrderTraversal(root))  # Output: [1, 2, 3, 4, 5]

values = [5, 4, 3, 2, 1]
head = createLinkedList(values)

root = constructBinaryTreeFromLinkedList(head)
print(levelOrderTraversal(root))  # Output: [5, 4, 3, 2, 1]
