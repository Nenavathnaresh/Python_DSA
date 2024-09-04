from collections import defaultdict

def atMostK(S, K):
    count = defaultdict(int)
    left = 0
    result = 0
    distinct_count = 0
    
    for right in range(len(S)):
        if count[S[right]] == 0:
            distinct_count += 1
        count[S[right]] += 1
        
        while distinct_count > K:
            count[S[left]] -= 1
            if count[S[left]] == 0:
                distinct_count -= 1
            left += 1
        
        result += right - left + 1
        
    return result

def substrCount(S, K):
    return atMostK(S, K) - atMostK(S, K-1)

# Example usage:
S = "abaaca"
K = 1
print(substrCount(S, K))  # Output: 7
