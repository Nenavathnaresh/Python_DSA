import heapq

def minCost(arr):
    # Create a min-heap from the array
    heapq.heapify(arr)
    
    total_cost = 0
    
    # Continue until only one rope is left
    while len(arr) > 1:
        # Extract the two smallest ropes
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        
        # Cost to connect the two ropes
        cost = first + second
        total_cost += cost
        
        # Insert the new combined rope back into the heap
        heapq.heappush(arr, cost)
    
    return total_cost

# Test cases
arr1 = [4, 3, 2, 6]
arr2 = [4, 2, 7, 6, 9]
print(minCost(arr1))  # Output: 29
print(minCost(arr2))  # Output: 62
