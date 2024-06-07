def combinationSum(arr, B):
    def backtrack(start, current_combination, current_sum):
        # Base case: if current_sum equals target sum B
        if current_sum == B:
            result.append(tuple(current_combination))
            return
        if current_sum > B:
            return
        
        for i in range(start, len(arr)):
            current_combination.append(arr[i])
            backtrack(i, current_combination, current_sum + arr[i])
            current_combination.pop()
    
    # Sort the array to handle duplicates and non-descending order
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    result = []
    backtrack(0, [], 0)
    
    # Remove duplicates by converting list of tuples to a set and back to list
    result = sorted(set(result))
    return result

# Example usage
N = 4
arr = [7, 2, 6, 5]
B = 16
print(combinationSum(arr, B))
# Output:
# [(2, 2, 2, 2, 2, 2, 2, 2), 
#  (2, 2, 2, 2, 2, 6), 
#  (2, 2, 2, 5, 5), 
#  (2, 2, 5, 7), 
#  (2, 2, 6, 6), 
#  (2, 7, 7), 
#  (5, 5, 6)]

N = 11
arr = [6, 5, 7, 1, 8, 2, 9, 9, 7, 7, 9]
B = 6
print(combinationSum(arr, B))
# Output:
# [(1, 1, 1, 1, 1, 1), 
#  (1, 1, 1, 1, 2), 
#  (1, 1, 2, 2), 
#  (1, 5), 
#  (2, 2, 2), 
#  (6)]
