def find_paths(mat):
    # Get the dimension of the matrix
    n = len(mat)
    
    # If the starting or ending cell is blocked, no path is possible
    if mat[0][0] == 0 or mat[n-1][n-1] == 0:
        return []

    # This list will store all the paths
    paths = []

    # Create a visited matrix initialized to False
    visited = [[False for _ in range(n)] for _ in range(n)]

    # Helper function to perform backtracking
    def backtrack(x, y, path):
        # If destination is reached, add the path to the list of paths
        if x == n-1 and y == n-1:
            paths.append(path)
            return

        # Possible directions in which the rat can move
        directions = {
            'D': (1, 0),  # Move Down
            'L': (0, -1), # Move Left
            'R': (0, 1),  # Move Right
            'U': (-1, 0)  # Move Up
        }

        # Mark the current cell as visited
        visited[x][y] = True

        # Explore all possible directions
        for direction in ['D', 'L', 'R', 'U']:
            dx, dy = directions[direction]
            new_x, new_y = x + dx, y + dy

            # Check if the new position is within bounds and not visited and not blocked
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y] and mat[new_x][new_y] == 1:
                backtrack(new_x, new_y, path + direction)

        # Unmark the current cell as visited for other paths
        visited[x][y] = False

    # Start the backtracking from the initial position (0, 0)
    backtrack(0, 0, '')

    # Sort paths lexicographically
    paths.sort()

    return paths

# Test cases
mat1 = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

mat2 = [
    [1, 0],
    [1, 0]
]

print(find_paths(mat1))  # Output: ['DDRDRR', 'DRDDRR']
print(find_paths(mat2))  # Output: []
