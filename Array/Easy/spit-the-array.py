MOD = 10**9 + 7

def countWays(arr):
    n = len(arr)
    
    # Step 1: Compute XOR of the entire array
    XOR_sum = 0
    for num in arr:
        XOR_sum ^= num
    
    # Step 2: If XOR of the entire array is not zero, return 0
    if XOR_sum != 0:
        return 0
    
    # Step 3: If XOR_sum is 0, calculate 2^(n-1) % MOD
    # We use fast exponentiation to compute (2^(n-1)) % MOD
    def power_of_two(exp, mod):
        result = 1
        base = 2
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result
    
    # Number of ways is 2^(n-1)
    return power_of_two(n-1, MOD)-1

# Example usage:
arr1 = [1, 2, 3]
print(countWays(arr1))  # Output: 3

arr2 = [5, 2, 3, 2]
print(countWays(arr2))  # Output: 0
