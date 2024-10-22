def longestIncreasingSubsequence(n, arr):
    if n == 0:
        return []
    
    # dp[i] will hold the length of the LIS ending at index i
    dp = [1] * n
    # parent[i] will help reconstruct the LIS path
    parent = [-1] * n
    
    # Fill the dp array and parent array
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                # In case of tie in dp[j] + 1 == dp[i], prefer the smaller index j
                # elif dp[j] + 1 == dp[i] and arr[j] < arr[parent[i]]:
                #     parent[i] = j

    # Find the index of the maximum length LIS
    lis_length = max(dp)
    lis_index = dp.index(lis_length)

    # Reconstruct the LIS using the parent array
    lis = []
    while lis_index != -1:
        lis.append(arr[lis_index])
        lis_index = parent[lis_index]

    # The lis array will be in reverse order, so reverse it
    lis.reverse()
    return lis
