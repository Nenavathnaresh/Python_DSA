def LCIS(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    
    # Create a dp array for arr2[] initialized to 0
    dp = [0] * m
    
    # Traverse arr1[] and arr2[] to find the LCIS
    for i in range(n):
        # Initialize current max to zero (since we are looking for increasing subsequences)
        current_max = 0
        for j in range(m):
            # If arr1[i] is equal to arr2[j], try to update dp[j]
            if arr1[i] == arr2[j]:
                dp[j] = max(dp[j], current_max + 1)
            # If arr1[i] is greater than arr2[j], update current_max
            if arr1[i] > arr2[j]:
                current_max = max(current_max, dp[j])
    
    # The maximum value in dp[] will be the length of the LCIS
    return max(dp)

# Example usage:
arr1 = [3, 4, 9, 1]
arr2 = [5, 3, 8, 9, 10, 2, 1]
print(LCIS(arr1, arr2))  # Output: 2

arr1 = [1, 1, 4, 3]
arr2 = [1, 1, 3, 4]
print(LCIS(arr1, arr2))  # Output: 2
