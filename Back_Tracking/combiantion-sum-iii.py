def combinationSum(K, N):
    def backtrack(start, current_combination, current_sum):
        # If the combination is of length K and the sum is N, we add it to the results
        if len(current_combination) == K and current_sum == N:
            result.append(list(current_combination))
            return
        # If the combination exceeds length K or the sum exceeds N, we stop
        if len(current_combination) > K or current_sum > N:
            return
        # Try to include numbers from start to 9
        for i in range(start, 10):
            current_combination.append(i)
            backtrack(i + 1, current_combination, current_sum + i)
            current_combination.pop()  # backtrack

    result = []
    backtrack(1, [], 0)
    return result

# Example Usage
K = 3
N = 7
print(combinationSum(K, N))  # Output: [[1, 2, 4]]

K = 3
N = 9
print(combinationSum(K, N))  # Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

K = 4
N = 3
print(combinationSum(K, N))  # Output: []
