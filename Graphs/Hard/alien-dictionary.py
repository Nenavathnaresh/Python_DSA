from collections import defaultdict, deque

def findOrder(words, N, K):
    # Step 1: Create graph
    graph = defaultdict(set)  # adjacency list for directed graph
    indegree = {chr(i + ord('a')): 0 for i in range(K)}  # indegree dictionary for K characters

    # Build the graph by comparing adjacent words
    for i in range(N - 1):
        word1, word2 = words[i], words[i + 1]
        min_length = min(len(word1), len(word2))
        
        # Compare characters of both words
        for j in range(min_length):
            if word1[j] != word2[j]:
                # If characters are different, add an edge and break
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    indegree[word2[j]] += 1
                break
    
    # Step 2: Topological Sort using Kahn's algorithm (BFS)
    queue = deque()
    
    # Add all nodes with indegree 0 to the queue
    for char in indegree:
        if indegree[char] == 0:
            queue.append(char)
    
    order = []
    
    while queue:
        char = queue.popleft()
        order.append(char)
        
        # Decrease indegree of neighbors
        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # If the length of the order is K, it means we found a valid order
    if len(order) == K:
        return ''.join(order)
    else:
        # Return empty string if there's a cycle (though this should not happen)
        return ""

# Test examples
dict1 = ["baa", "abcd", "abca", "cab", "cad"]
N1, K1 = 5, 4
print(findOrder(dict1, N1, K1))  # Possible outputs: "bdac", "bcda", etc.

dict2 = ["caa", "aaa", "aab"]
N2, K2 = 3, 3
print(findOrder(dict2, N2, K2))  # Possible output: "cab"
