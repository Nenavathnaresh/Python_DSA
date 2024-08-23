def bpm(G, u, matchR, seen):
    # Try every job one by one
    for v in range(len(G[0])):
        # If applicant u is interested in job v and v is not seen yet
        if G[u][v] and not seen[v]:
            seen[v] = True  # Mark v as seen
            
            # If job v is not assigned to an applicant OR
            # previously assigned applicant for job v (which is matchR[v]) has an alternate job available.
            if matchR[v] == -1 or bpm(G, matchR[v], matchR, seen):
                matchR[v] = u  # Assign job v to applicant u
                return True
    return False

def maximumMatch(G):
    M = len(G)  # Number of applicants
    N = len(G[0])  # Number of jobs
    
    # matchR[i] is the applicant assigned to job i, -1 if no one is assigned
    matchR = [-1] * N
    
    result = 0  # Count of jobs assigned to applicants
    
    # Iterate over each applicant
    for i in range(M):
        seen = [False] * N  # Mark all jobs as not seen for next applicant
        if bpm(G, i, matchR, seen):
            result += 1
    
    return result

# Example usage:
M = 3
N = 5
G = [[1, 1, 0, 1, 1],
     [0, 1, 0, 0, 1],
     [1, 1, 0, 1, 1]]

print(maximumMatch(G))  # Output: 3

M = 6
N = 2
G = [[1, 1],
     [0, 1],
     [0, 1],
     [0, 1],
     [0, 1],
     [1, 0]]

print(maximumMatch(G))  # Output: 2
