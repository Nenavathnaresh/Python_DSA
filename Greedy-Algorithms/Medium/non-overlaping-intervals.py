class Solution:
    def minRemoval(self, N: int, intervals):
        # Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        
        # Initialize the count of non-overlapping intervals
        non_overlap_count = 0
        
        # Start with the earliest end time
        current_end = float('-inf')
        
        # Iterate over each interval
        for start, end in intervals:
            # If the current interval does not overlap, select it
            if start >= current_end:
                non_overlap_count += 1
                current_end = end
        
        # Minimum removals required to achieve non-overlapping intervals
        return N - non_overlap_count

# Example Usage:
# sol = Solution()
# print(sol.minRemoval(4, [[1, 2], [2, 3], [3, 4], [1, 3]]))  # Output: 1
# print(sol.minRemoval(3, [[1, 3], [1, 3], [1, 3]]))          # Output: 2
