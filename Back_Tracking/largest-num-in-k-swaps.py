def findMaximumNum(self,str, K):
    # Helper function to perform recursive swaps
    def find_maximum(s, k, idx):
        if k == 0 or idx == len(s):
            return
        max_digit = max(s[idx:])
        if max_digit != s[idx]:
            k -= 1
        
        # Swap only if the current digit is not already the maximum digit
        for i in range(idx, len(s)):
            if s[i] == max_digit:
                # Swap the current index with the index of max_digit found
                s[idx], s[i] = s[i], s[idx]
                current_num = ''.join(s)
                
                # Update the maximum number found so far
                if current_num > self.max_number:
                    self.max_number = current_num
                
                # Recurse with reduced swaps and next index
                find_maximum(s, k, idx + 1)
                
                # Backtrack to restore original string
                s[idx], s[i] = s[i], s[idx]

    # Initial setup
    self.max_number = str
    find_maximum(list(str), K, 0)
    return self.max_number

# Example usage:
print(findMaximumNum("1234567", 4))  # Output: "7654321"
print(findMaximumNum("3435335", 3))  # Output: "5543333"

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

def findMaximumNum(str, K):
    # Helper function to perform recursive swaps
    def find_maximum(s, k, max_so_far):
        if k == 0:
            return max_so_far
        n = len(s)
        for i in range(n-1):
            for j in range(i+1, n):
                if s[j] > s[i]:
                    # Swap characters at positions i and j
                    s[i], s[j] = s[j], s[i]
                    # Form the new number and check if it's the largest so far
                    new_num = ''.join(s)
                    if new_num > max_so_far:
                        max_so_far = new_num
                    # Recurse with one less swap available
                    max_so_far = find_maximum(s, k-1, max_so_far)
                    # Backtrack to the previous state
                    s[i], s[j] = s[j], s[i]
        return max_so_far
    
    max_number = find_maximum(list(str), K, str)
    return max_number

# Example usage:
print(findMaximumNum("1234567", 4))  # Output: "7654321"
print(findMaximumNum("3435335", 3))  # Output: "5543333"

