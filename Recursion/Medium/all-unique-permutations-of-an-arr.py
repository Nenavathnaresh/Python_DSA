from itertools import permutations

def uniquePerms(arr):
    # Generate all permutations using itertools.permutations
    perm = permutations(arr)
    
    # Use a set to filter out duplicate permutations
    unique_perm_set = set(perm)
    
    # Convert the set to a list and sort it
    unique_perm_list = sorted(list(unique_perm_set))
    
    # Convert each tuple to a list (as required by the output format)
    unique_perm_list = [list(p) for p in unique_perm_list]
    
    return unique_perm_list

# Example usage:
n = 3
arr = [1, 2, 1]
print(uniquePerms(arr))

n = 2
arr = [4, 5]
print(uniquePerms(arr))
