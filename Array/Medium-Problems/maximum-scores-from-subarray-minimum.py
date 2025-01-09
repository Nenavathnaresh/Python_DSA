def pairWithMaxSum(self, arr):
        # Your code goes here
    n = len(arr)
    max_sum = 0
    for i in range(1,n):
        curr_sum = arr[i-1] + arr[i]
        max_sum = max(max_sum, curr_sum)
    return max_sum