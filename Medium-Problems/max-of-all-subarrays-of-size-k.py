from collections import deque

def max_of_subarrays(arr, n, k):
    # Result array to store the maximum of each subarray
    result = []
    
    # Deque to store indices of array elements
    deq = deque()
    
    for i in range(n):
        # Remove elements not in the current window
        if deq and deq[0] == i - k:
            deq.popleft()
        
        # Remove elements that are less than the current element from the deque
        while deq and arr[deq[-1]] <= arr[i]:
            deq.pop()
        
        # Add current element at the back of the deque
        deq.append(i)
        
        # The front of the deque is the maximum of the current window
        if i >= k - 1:
            result.append(arr[deq[0]])
    
    return result

# Example usage:
N = 9
K = 3
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
print(max_of_subarrays(arr, N, K))  # Output: [3, 3, 4, 5, 5, 5, 6]

N = 10
K = 4
arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
print(max_of_subarrays(arr, N, K))  # Output: [10, 10, 10, 15, 15, 90, 90]
