def maxEqualSum(N1, N2, N3, S1, S2, S3):
    # Calculate initial sums of the stacks
    sum1, sum2, sum3 = sum(S1), sum(S2), sum(S3)
    
    # Initialize pointers for each stack
    i, j, k = 0, 0, 0
    
    while i < N1 and j < N2 and k < N3:
        # If all sums are equal, return any of them
        if sum1 == sum2 == sum3:
            return sum1
        
        # Find the stack with the maximum sum and remove its top element
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= S1[i]
            i += 1
        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= S2[j]
            j += 1
        elif sum3 >= sum1 and sum3 >= sum2:
            sum3 -= S3[k]
            k += 1
    
    # If we exit the loop, it means one of the stacks is exhausted and sums cannot be equalized
    return 0

# Example usage:
N1, N2, N3 = 3, 4, 2
S1 = [4, 2, 3]
S2 = [1, 1, 2, 3]
S3 = [1, 4]
print(maxEqualSum(N1, N2, N3, S1, S2, S3))  # Output: 5

N1, N2, N3 = 2, 1, 3
S1 = [4, 7]
S2 = [10]
S3 = [1, 2, 3]
print(maxEqualSum(N1, N2, N3, S1, S2, S3))  # Output: 0
