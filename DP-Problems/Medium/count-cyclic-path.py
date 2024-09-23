MOD = 10**9 + 7

def countPaths(N):
    # Base cases: At step 0, the person is at O.
    dpO, dpA, dpB, dpC = 1, 0, 0, 0
    
    for i in range(1, N + 1):
        new_dpO = (dpA + dpB + dpC) % MOD
        new_dpA = (dpO + dpB + dpC) % MOD
        new_dpB = (dpO + dpA + dpC) % MOD
        new_dpC = (dpO + dpA + dpB) % MOD
        
        dpO, dpA, dpB, dpC = new_dpO, new_dpA, new_dpB, new_dpC
    
    return dpO

# Example usage:
N1 = 1
print(countPaths(N1))  # Output: 0

N2 = 2
print(countPaths(N2))  # Output: 3


