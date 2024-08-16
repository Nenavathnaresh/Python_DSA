from typing import List
from collections import deque

class Solution:
    def __init__(self):
        self.rowNum = [-1, 0, 0, 1]
        self.colNum = [0, -1, 1, 0]
        
    def findShortestPath(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        
        # Queue to perform BFS
        q = deque()
        
        # Distance array to store shortest distance
        d = [[float('inf')] * m for _ in range(n)]
        
        # Function to check if cell is valid
        def isValid(i, j):
            return 0 <= i < n and 0 <= j < m

        
        # Function to check if cell and its adjacent cells are safe
        def check(i, j):
            if not isValid(i, j):
                return False
            for k in range(4):
                if isValid(i + self.rowNum[k], j + self.colNum[k]) and mat[i + self.rowNum[k]][j + self.colNum[k]] == 0:
                    return False
            return True
        
        # Pushing cells from the rightmost column into the queue
        for i in range(n):
            if check(i, m - 1):
                q.append((i, m - 1, 1))
        
        # BFS traversal
        while q:
            x, y, dis = q.popleft()
            if d[x][y] > dis:
                d[x][y] = dis
                for k in range(4):
                    if check(x + self.rowNum[k], y + self.colNum[k]):
                        q.append((x + self.rowNum[k], y + self.colNum[k], dis + 1))
        
        # Finding the minimum distance in the first column
        ans = float('inf')
        for i in range(n):
            ans = min(ans, d[i][0])
        
        # If no safe path found, return -1
        if ans == float('inf'):
            return -1
        return ans