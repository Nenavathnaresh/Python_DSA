MOD = 10**9 + 7

def fun(S):
    count_a = 0
    count_ab = 0
    count_abc = 0
    
    for char in S:
        if char == 'a':
            # Every new 'a' can start a new subsequence or extend existing ones
            count_a = (2 * count_a + 1) % MOD
        elif char == 'b':
            # Every new 'b' can attach to existing subsequences of 'a'
            count_ab = (2 * count_ab + count_a) % MOD
        elif char == 'c':
            # Every new 'c' can attach to existing subsequences of 'ab'
            count_abc = (2 * count_abc + count_ab) % MOD
    
    return count_abc
