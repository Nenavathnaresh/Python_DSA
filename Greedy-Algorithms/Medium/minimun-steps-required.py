def minSteps(str):
    if not str:
        return 0

    # Initialize the number of groups to 1 (since the first character forms a group)
    group_count = 1
    
    # Traverse the string starting from the second character
    for i in range(1, len(str)):
        # If the current character is different from the previous one, it's a new group
        if str[i] != str[i - 1]:
            group_count += 1
    
    # Since each transition between 'a' and 'b' forms a new group,
    # the number of operations needed is the number of transitions
    return group_count // 2 + 1

# Example usage
print(minSteps("bbaaabb"))  # Output: 2
print(minSteps("aababaa"))  # Output: 3
