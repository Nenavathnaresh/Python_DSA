from collections import deque

def max_of_subarrays(arr, n, k):
    # Deque to store indices of array elements
    dq = deque()
    result = []
    
    for i in range(n):
        # Remove elements from the front if they are out of the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove elements from the back while the current element is larger
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        
        # Add the current element's index to the deque
        dq.append(i)
        
        # If we have processed at least k elements, the front of the deque is the max for this window
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result
