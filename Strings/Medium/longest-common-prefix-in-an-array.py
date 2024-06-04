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
