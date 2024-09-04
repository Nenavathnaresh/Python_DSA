class Solution:
    def maxDotProduct(self, n, m, a, b):
        # Create 2D Matrix that stores dot product
        # dp[i+1][j+1] stores product considering b[0..i]
        # and a[0...j]. Note that since all m > n, we fill
        # values in upper diagonal of dp[][]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Traverse through all elements of B[]
        for i in range(1, m + 1):

            # Consider all values of a[] with indexes greater
            # than or equal to i and compute dp[i][j]
            for j in range(i, n + 1):

                # Two cases arise
                # 1) Include a[j]
                # 2) Exclude a[j] (insert 0 in b[])
                dp[i][j] = max(dp[i - 1][j - 1] + (a[j - 1] * b[i - 1]), dp[i][j - 1])

        # Return Maximum Dot Product
        return dp[m][n]

##############################################################################################

class Solution:
    def maxDotProduct(self, n, m, A, B):
        # Function to calculate the dot product of two arrays
        def product(p1, p2):
            summe = 0
            # Iterate through both arrays and calculate the sum of products
            while(p1 < n and p2 < m):
                summe += (A[p1] * B[p2])
                p1 += 1
                p2 += 1
            return summe
        
        # Recursive function to solve the problem
        def solve(p1, p2):
            # Base case: if either array is fully traversed, return 0
            if (p1 == n and p2 == m) or (p2 == m):
                return 0
            # Base case: if one array is fully traversed, return negative infinity
            if (p1 == n):
                return float('-inf')
            # Check if subproblem has already been solved
            key = str(p1) + "_" + str(p2)
            if (key in dp):
                return dp[key]
            # Calculate maximum dot product considering two cases:
            # 1. Include the current elements and move to the next elements in both arrays
            not_zero = A[p1] * B[p2] + solve(p1 + 1, p2 + 1)
            
            # 2. Do not include the current element in array A and move to the next element in array A
            zero = solve(p1 + 1, p2)
            
            # Store the maximum dot product in the dp dictionary
            dp[key] = max(zero, not_zero)
            return dp[key]
        
        # Calculate the difference in length between arrays A and B
        diff = n - m
        # If both arrays have the same length, directly calculate the dot product
        if (diff == 0):
            return product(0, 0)
        else:
            # Initialize a dp dictionary to store results of subproblems
            dp = {}
            # Solve the problem recursively and return the maximum dot product
            ans = solve(0, 0)
            return ans