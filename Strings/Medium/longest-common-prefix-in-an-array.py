def longestCommonPrefix(arr, N):
    # If the array is empty, return "-1"
    if N == 0:
        return "-1"
    
    # Start with the first string as the prefix
    prefix = arr[0]
    
    # Compare the prefix with each string
    for i in range(1, N):
        current_string = arr[i]
        j = 0
        
        # Compare characters until a mismatch is found or end of any string is reached
        while j < len(prefix) and j < len(current_string) and prefix[j] == current_string[j]:
            j += 1
        
        # Update the prefix to the matched portion
        prefix = prefix[:j]
        
        # If at any point, the prefix becomes empty, there is no common prefix
        if prefix == "":
            return "-1"
    
    # Return the longest common prefix found
    return prefix

# Example usage
arr1 = ["geeksforgeeks", "geeks", "geek", "geezer"]
N1 = 4
print(longestCommonPrefix(arr1, N1))  # Output: "gee"

arr2 = ["hello", "world"]
N2 = 2
print(longestCommonPrefix(arr2, N2))  # Output: "-1"


############################ Second method ###################################

def longest_common_prefix(arr):
    if not arr:
        return "-1"
    
    # Start with the first string as the initial prefix
    prefix = arr[0]
    
    # Find the minimum length string in the array
    min_length = min(len(s) for s in arr)
    
    # Iterate through each character index up to the minimum length
    for i in range(min_length):
        # Check the i-th character of each string
        current_char = prefix[i]
        for s in arr:
            if s[i] != current_char:
                # If a mismatch is found, return the prefix up to this point
                if i == 0:
                    return "-1"
                return prefix[:i]
    
    # Return the prefix up to the minimum length
    return prefix[:min_length]

# Example 1
arr1 = ["geeksforgeeks", "geeks", "geek", "geezer"]
output1 = longest_common_prefix(arr1)
print(output1)  # Output: gee

# Example 2
arr2 = ["hello", "world"]
output2 = longest_common_prefix(arr2)
print(output2)  # Output: -1


######################################### third method ######################################

def longest_common_prefix(arr):
    if not arr:
        return "-1"
    
    # Start with the first string as the prefix
    prefix = arr[0]
    
    # Compare the prefix with each string in the array
    for s in arr[1:]:
        # Reduce the prefix size until it matches the current string
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return "-1"
    
    return prefix

# Example 1
arr1 = ["geeksforgeeks", "geeks", "geek", "geezer"]
output1 = longest_common_prefix(arr1)
print(output1)  # Output: gee

# Example 2
arr2 = ["hello", "world"]
output2 = longest_common_prefix(arr2)
print(output2)  # Output: -1

