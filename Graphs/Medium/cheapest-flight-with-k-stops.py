import heapq
import collections

def findCheapestPrice(n, flights, src, dst, k):
    # Create an adjacency list
    adj = collections.defaultdict(list)
    for u, v, price in flights:
        adj[u].append((v, price))
    
    # Priority queue: (cost, node, stops)
    pq = [(0, src, 0)]
    # Cost table with infinity initialization
    cost = [(float('inf'), float('inf'))] * n
    
    # Process nodes in the priority queue
    while pq:
        current_cost, node, stops = heapq.heappop(pq)
        
        # If we reached the destination and within k stops, return the cost
        if node == dst:
            return current_cost
        
        # If stops are within the limit, explore neighbors
        if stops <= k:
            for neighbor, price in adj[node]:
                new_cost = current_cost + price
                # Push to the priority queue if it's a cheaper path or fewer stops
                if new_cost < cost[neighbor][0] or stops + 1 < cost[neighbor][1]:
                    heapq.heappush(pq, (new_cost, neighbor, stops + 1))
                    cost[neighbor] = (new_cost, stops + 1)
    
    # If the destination was never reached within k stops, return -1
    return -1

# Example usage:
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))  # Output: 700
