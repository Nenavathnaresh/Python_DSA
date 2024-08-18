import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict

# Despite defining recursive depth limit as 1e6, we get maximum allowed depth of 3e3.
# So, for this algorithm, we will be using iterative approach of DFS over recursive approach.


class Solution:
    maxn = 1000001
    a = [0]*(maxn+1)
    pl = [2];

    def precompute(self):
        for i in range(1, self.maxn+1):
            self.a[i] = 1

        self.a[0] = 0
        self.a[1] = 0

        i = 2
        while i*i<=self.maxn:
            if(self.a[i]==1):
                j = i*i
                while j<=self.maxn:
                    self.a[j] = 0
                    j+=i
            i+=1

        for i in range(3, self.maxn+1):
            if(self.a[i]):
                self.pl.append(i)

    def helpSanta(self, n, m, g):
        graph = defaultdict(list)
        for x,y in g:
            graph[x].append(y)
            graph[y].append(x)
        vis = [0] * (n + 1)
        lc = 0

        for i in range(1, n + 1):
            if not vis[i]:
                
                # Push first index to be processed in DFS to the stack
                stack = [i]
                vis[i] = 1
                cnt = 1

                # While we have elements to process in stack, i.e., while DFS is being called, we will be in the while loop
                while stack: 
                    node = stack.pop()

                    # Pushing more elements in the stack, i.e., calling for more DFS calls
                    for x in graph[node]:
                        if not vis[x]:
                            stack.append(x)
                            vis[x] = 1
                            cnt += 1

                lc = max(lc, cnt)

        if lc == 1:
            return -1

        return self.pl[lc-1]
    
    ##########################################################################

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            for multiple in range(i * i, limit + 1, i):
                is_prime[multiple] = False
                
    return primes

def dfs(node, adj, visited):
    stack = [node]
    size = 0
    while stack:
        curr = stack.pop()
        if not visited[curr]:
            visited[curr] = True
            size += 1
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    return size

def helpSanta(n, m, g):
    if m == 0:
        return -1
    
    # Create the adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for u, v in g:
        adj[u].append(v)
        adj[v].append(u)
    
    # Find the largest connected component
    visited = [False] * (n + 1)
    max_group_size = 0
    
    for girl in range(1, n + 1):
        if not visited[girl]:
            component_size = dfs(girl, adj, visited)
            max_group_size = max(max_group_size, component_size)
    
    # Precompute primes
    limit = 1000000
    primes = sieve_of_eratosthenes(limit)
    
    # Return the Kth prime where K is max_group_size
    return primes[max_group_size - 1]

# Example usage
N = 10
M = 6
g = [[1,2],[2,3],[3,4],[4,5],[6,7],[9,10]]
print(helpSanta(N, M, g))  # Output: 11
