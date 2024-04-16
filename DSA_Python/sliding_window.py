############################# Sliding window ##################################################

#%%%%%%%%%%%%%%%%%%%%%%%%%%    1   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def maxSum(arr,n,k):
    maxSum = float("-inf")
    for i in range(n-k + 1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i+j]
        maxSum = max(maxSum, current_sum)
    return maxSum
arr = [1,4,2,10,2,3,1,0,20]
k = 4 
n = len(arr)
print(maxSum(arr,n,k))

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     2    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def MS(arr,n,k):
    ms = 0
    for i in range(k):
        ms += arr[i]
    ws = ms
    for i in range(k,n):
        ws = ws - arr[i-k] + arr[i]
        ms = max(ms, ws)
    return ms 

arr = [1,4,2,10,2,3,1,0,20]
k = 4 
n = len(arr)
print(MS(arr,n,k))

# %%%%%%%%%%%%%%%%%%%%%%%%%%    3      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def max_sum_subarray(arr, k):
    n = len(arr)
    max_sum = float('-inf')
    window_sum = 0
    left = 0

    for right in range(n):
        # Add the element at the right pointer to the window sum
        window_sum += arr[right]
        
        # Check if the window size is greater than k
        if right - left + 1 > k:
            # Subtract the element at the left pointer from the window sum
            window_sum -= arr[left]
            # Move the left pointer to the right
            left += 1
        
        # Update the max_sum
        max_sum = max(max_sum, window_sum)
    
    return max_sum
arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
k = 3
print(max_sum_subarray(arr, k))  # Output: 16 (subarray [7, 8, 1] has the maximum sum)
