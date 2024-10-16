def canBeSortedInTwoSwaps(arr):
    # Create a sorted version of the array
    sorted_arr = sorted(arr)
    
    # Find mismatched positions
    mismatches = []
    
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            mismatches.append(i)
    
    # Check if there are exactly 4 mismatches (2 swaps needed to sort)
    if len(mismatches) == 4:
        # We need to verify if swapping can actually sort the array
        # Perform the two possible swaps and check if the array becomes sorted
        i1, i2, i3, i4 = mismatches
        
        # Swap i1 and i4, then i2 and i3
        arr_after_first_swap = arr[:]
        arr_after_first_swap[i1], arr_after_first_swap[i4] = arr_after_first_swap[i4], arr_after_first_swap[i1]
        arr_after_first_swap[i2], arr_after_first_swap[i3] = arr_after_first_swap[i3], arr_after_first_swap[i2]
        
        # Check if array is sorted after the two swaps
        return arr_after_first_swap == sorted_arr
    
    # If there are not exactly 4 mismatches, return False
    return False
