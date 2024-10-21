# #Back-end complete function Template for Python 3
# from heapq import heappush, heappop


# class Compare:

#     def __init__(self, node):
#         self.node = node

#     def __lt__(self, other):
#         return self.node.data < other.node.data


# class Solution:
#     # Function to sort a k-sorted doubly linked list
#     def sortAKSortedDLL(self, head, k):
#         # If the list is empty
#         if head is None:
#             return head

#         # Min-heap to sort the DLL nodes
#         pq = []

#         # Create a Min Heap of first (k+1) elements from the input doubly linked list
#         newHead = None
#         last = None
#         for i in range(k + 1):
#             if head is not None:
#                 heapq.heappush(pq, Compare(head))
#                 head = head.next

#         # Process the heap and sort the linked list
#         while pq:
#             min_node = heapq.heappop(pq).node

#             if newHead is None:
#                 newHead = min_node
#                 newHead.prev = None
#                 last = newHead
#             else:
#                 last.next = min_node
#                 min_node.prev = last
#                 last = min_node

#             # If there are more nodes left in the input list
#             if head is not None:
#                 heapq.heappush(pq, Compare(head))
#                 head = head.next

#         # Set the last node's next to None
#         last.next = None

#         return newHead