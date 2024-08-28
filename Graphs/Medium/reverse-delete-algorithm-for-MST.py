from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)
        self.edges = []

    def add_edge(self, u, v, w):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.edges.append((w, u, v))

    def DFS(self, v, visited):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                self.DFS(i, visited)

    def is_connected(self):
        visited = [False] * self.V
        self.DFS(0, visited)
        for i in range(1, self.V):
            if not visited[i]:
                return False
        return True

    def reverse_delete_mst(self):
        self.edges.sort(reverse=True)
        mst_wt = 0

        for w, u, v in self.edges:
            self.adj[u].remove(v)
            self.adj[v].remove(u)

            if not self.is_connected():
                self.adj[u].append(v)
                self.adj[v].append(u)
                mst_wt += w

        return mst_wt

class Solution:
    def RevDelMST(self, Arr, V, E):
        g = Graph(V)
        
        for i in range(0, 3*E, 3):
            g.add_edge(Arr[i], Arr[i+1], Arr[i+2])
            
        return g.reverse_delete_mst()
