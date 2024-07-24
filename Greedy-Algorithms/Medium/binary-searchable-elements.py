from typing import List

class Solution:
    def binarySearchable(self, n: int, arr: List[int]) -> int:
        # Step 1: Initialize max_left and min_right arrays
        max_left = [float('-inf')] * n
        min_right = [float('inf')] * n
        
        # Step 2: Fill the max_left array
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], arr[i - 1])
        
        # Step 3: Fill the min_right array
        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], arr[i + 1])
        
        # Step 4: Count binary searchable elements
        count = 0
        for i in range(n):
            if max_left[i] < arr[i] < min_right[i]:
                count += 1
        
        return count

# Example Usage:
sol = Solution()
print(sol.binarySearchable(3, [1, 3, 2]))  # Output: 1
print(sol.binarySearchable(6, [2, 1, 3, 5, 4, 6]))  # Output: 2
