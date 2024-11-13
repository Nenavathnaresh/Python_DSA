class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        n = len(arr)
        ans = 0 
        for i in range(1,n):
            if arr[i] <= arr[i-1]:
                ans += (arr[i-1] - arr[i] + 1)
                arr[i] = arr[i-1] + 1 
        return ans