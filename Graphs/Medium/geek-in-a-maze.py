import heapq as hq


#Function to check if given coordinate is valid or not.
def isValid(row, col, n, m):
    if 0 <= row < n and 0 <= col < m:
        return True


#Function to find the number of cells accessible from given coordinates.
def numberOfCells(n, m, r, c, u, d, mat):

    #If the starting cell is a block, return 0.
    if mat[r][c] == '#':
        return 0

    #Using a priority queue to store cells based on their priority.
    pque = []
    #Creating a matrix to keep track of visited cells.
    vis = [[0 for i in range(m)] for j in range(n)]

    #Pushing the starting cell into the priority queue.
    hq.heappush(pque, ((0, 0), (r, c)))
    vis[r][c] = 1

    #Iterating until the priority queue is empty.
    while pque:
        up, down = pque[0][0][0], pque[0][0][1]

        x, y = pque[0][1][0], pque[0][1][1]

        #Removing the cell with highest priority from the priority queue.
        hq.heappop(pque)

        #Checking all the adjacent cells and adding them to the priority queue if they meet the conditions.
        if isValid(x - 1, y, n, m):
            if up + 1 <= u and not vis[x - 1][y] and down <= d and mat[x - 1][y] == '.':
                hq.heappush(pque, (((up + 1), down), (x - 1, y)))
                vis[x - 1][y] = 1

        if isValid(x + 1, y, n, m):

            if down + 1 <= d and not vis[x + 1][y] and up <= u and mat[x + 1][y] == '.':
                hq.heappush(pque, ((up, (down + 1)), (x + 1, y)))
                vis[x + 1][y] = 1

        if isValid(x, y - 1, n, m):
            if down <= d and not vis[x][y - 1] and up <= u and mat[x][y - 1] == '.':
                hq.heappush(pque, ((up, down), (x, y - 1)))
                vis[x][y - 1] = 1

        if isValid(x, y + 1, n, m):
            if down <= d and not vis[x][y + 1] and up <= u and mat[x][y + 1] == '.':
                hq.heappush(pque, ((up, down), (x, y + 1)))
                vis[x][y + 1] = 1

    #Counting the number of visited cells.
    ans = 0
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 1:
                ans += 1

    #Returning the total number of accessible cells.
    return ans