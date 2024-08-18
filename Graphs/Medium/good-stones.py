def badStones(n, arr):
    state = [0] * n  # 0 = unvisited, 1 = bad stone, 2 = good stone

    def dfs(i):
        if i < 0 or i >= n:  # Out of bounds, it's a good path
            return 2
        if state[i] != 0:  # Already visited
            return state[i]
        
        # Mark as visiting (temporary mark)
        state[i] = 1
        
        next_position = i + arr[i]
        # Recur for the next position
        result = dfs(next_position)
        
        if result == 2:
            state[i] = 2  # Mark this stone as good
        return state[i]
    
    for i in range(n):
        if state[i] == 0:
            dfs(i)
    
    # Count the number of good stones
    return sum(1 for s in state if s == 2)

# Example usage:
arr1 = [2, 3, -1, 2, -2, 4, 1]
print(badStones(len(arr1), arr1))  # Output: 3

arr2 = [1, 0, -3, 0, -5, 0]
print(badStones(len(arr2), arr2))  # Output: 2
