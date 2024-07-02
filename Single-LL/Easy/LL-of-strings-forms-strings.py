class ListNode:
    def __init__(self, data=''):
        self.data = data
        self.next = None

def isPalindrome(head):
    # Step 1: Traverse the linked list and form the combined string
    combined_string = ""
    current = head
    while current:
        combined_string += current.data
        current = current.next
    
    # Step 2: Check if the combined string is a palindrome
    return combined_string == combined_string[::-1]

# Helper function to create a linked list from a list of strings
def createLinkedList(strings):
    if not strings:
        return None
    head = ListNode(strings[0])
    current = head
    for string in strings[1:]:
        current.next = ListNode(string)
        current = current.next
    return head

# Example usage:
# Test Case 1: Palindrome combined string
strings1 = ["abc", "dd", "cba"]
head1 = createLinkedList(strings1)
print(isPalindrome(head1))  # Output: True

# Test Case 2: Non-palindrome combined string
strings2 = ["abc", "d", "ba"]
head2 = createLinkedList(strings2)
print(isPalindrome(head2))  # Output: False
