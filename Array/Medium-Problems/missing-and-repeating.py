def find_missing_and_repeating(arr):
    n = len(arr)
    
    # Expected sum and square sum for numbers from 1 to n
    S = n * (n + 1) // 2
    S_square = n * (n + 1) * (2 * n + 1) // 6
    
    # Actual sum and square sum of the array
    sum_array = sum(arr)
    sum_square_array = sum(x * x for x in arr)
    
    # Calculate differences
    sum_diff = S - sum_array  # A - B
    square_sum_diff = S_square - sum_square_array  # A^2 - B^2
    
    # A + B = square_sum_diff / sum_diff
    sum_AB = square_sum_diff // sum_diff
    
    # Now, solve for A and B
    A = (sum_diff + sum_AB) // 2
    B = A - sum_diff
    
    return B, A

# Test cases
print(find_missing_and_repeating([2, 2]))  # Output: (2, 1)
print(find_missing_and_repeating([1, 3, 3]))  # Output: (3, 2)

##########################################################################################

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n = len(arr)
        dic = {}
        for i in range(n):
            if arr[i] in dic:
                dic[arr[i]] += 1
            else:
                dic[arr[i]] = 1
        rep_ind = 0
        for k,v in dic.items():
            if v == 2:
                rep_ind = k
        
        arr_sum = sum(arr)-rep_ind
        total_sum = n * (n+1) // 2
        
        return rep_ind, total_sum - arr_sum