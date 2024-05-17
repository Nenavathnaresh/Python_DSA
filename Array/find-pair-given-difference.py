class Solution:
    def findPair(self, n, arr, x):
        # Sort the array
        arr.sort()
        
        # Initialize two pointers
        left = 0
        right = 1
        
        # Iterate until the right pointer reaches the end of the array
        while right < n:
            if left != right and abs(arr[right] - arr[left]) == x:
                return 1
            elif abs(arr[right] - arr[left]) < x:
                right += 1
            else:
                left += 1
            
            # Ensure the two pointers don't cross each other
            if left == right:
                right += 1
        
        return -1

# Example usage:
sol = Solution()
print(sol.findPair(6, [5, 20, 3, 2, 5, 80], 78))  # Output: 1
print(sol.findPair(5, [90, 70, 20, 80, 50], 45))  # Output: -1
