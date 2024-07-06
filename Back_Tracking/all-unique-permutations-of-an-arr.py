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


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ without usign permutations @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def uniquePerms(arr):
    def backtrack(start):
        if start == len(arr):
            # Convert the current permutation to a tuple and add to the set
            unique_perms.add(tuple(arr))
            return
        for i in range(start, len(arr)):
            # Swap the current element with the element at the starting index
            arr[start], arr[i] = arr[i], arr[start]
            # Recurse on the next part of the array
            backtrack(start + 1)
            # Backtrack by swapping the elements back to their original positions
            arr[start], arr[i] = arr[i], arr[start]

    # Initialize a set to store unique permutations
    unique_perms = set()
    # Start the backtracking process from the first index
    backtrack(0)
    # Convert the set of tuples back to a sorted list of lists
    result = sorted([list(p) for p in unique_perms])
    return result

# Example usage:
n = 3
arr = [1, 2, 1]
print(uniquePerms(arr))

n = 2
arr = [4, 5]
print(uniquePerms(arr))
