def lengthOfLongestAP(arr, n):
    if n <= 1:
        return n
    
    # Create a dp table and initialize all values to 2
    dp = [[2 for _ in range(n)] for _ in range(n)]
    
    # Variable to store the result
    max_len = 2
    
    # Traverse the array from the second last element
    for j in range(n-2, -1, -1):
        i = j - 1
        k = j + 1
        
        # Check for pairs (i, j, k) that form an AP
        while i >= 0 and k < n:
            if arr[i] + arr[k] == 2 * arr[j]:
                # We found an AP, so update dp[i][j]
                dp[i][j] = dp[j][k] + 1
                # Update the max length
                max_len = max(max_len, dp[i][j])
                # Move both pointers
                i -= 1
                k += 1
            elif arr[i] + arr[k] < 2 * arr[j]:
                # Increment k if arr[i] + arr[k] < 2 * arr[j]
                k += 1
            else:
                # Decrement i if arr[i] + arr[k] > 2 * arr[j]
                i -= 1
    
    return max_len

# Example usage:
arr1 = [1, 7, 10, 13, 14, 19]
n1 = len(arr1)
print(lengthOfLongestAP(arr1, n1))  # Output: 4

arr2 = [2, 4, 6, 8, 10]
n2 = len(arr2)
print(lengthOfLongestAP(arr2, n2))  # Output: 5
