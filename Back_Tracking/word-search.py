def isWordExist(board, word):
    rows, cols = len(board), len(board[0])
    
    def dfs(i, j, word_index):
        # If the entire word is found
        if word_index == len(word):
            return True
        
        # Check boundaries and character match
        if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[word_index]:
            return False
        
        # Save the current cell value and mark as visited
        temp = board[i][j]
        board[i][j] = '#'
        
        # Explore all possible directions (up, down, left, right)
        found = (dfs(i+1, j, word_index+1) or
                 dfs(i-1, j, word_index+1) or
                 dfs(i, j+1, word_index+1) or
                 dfs(i, j-1, word_index+1))
        
        # Restore the current cell value
        board[i][j] = temp
        
        return found
    
    # Start from every cell
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    
    return False

# Test cases
print(isWordExist([['a','g','b','c'],['q','e','e','l'],['g','b','k','s']], "geeks"))  # Output: True
print(isWordExist([['a','b','c','e'],['s','f','c','s'],['a','d','e','e']], "sabfs"))  # Output: False
