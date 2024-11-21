class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        dic = {}
        res = []
        n = len(arr) // 3
        
        for vote in arr:
            if vote in dic:
                dic[vote] += 1
            else:
                dic[vote] = 1
        
        for k,v in dic.items():
            if v > n:
                res.append(k)
        
          
        return sorted(res)
    
    ###########################################################################


def majorityElement(arr):
    n = len(arr)
    if n == 0:
        return []

    # Step 1: Candidate selection
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0

    for num in arr:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Step 2: Verify the candidates
    count1, count2 = 0, 0
    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    # Step 3: Return in increasing order
    return sorted(result)

# Example usage
print(majorityElement([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]))  # Output: [5, 6]
print(majorityElement([1, 2, 3, 4, 5]))                   # Output: []
print(majorityElement([3, 2, 3]))                         # Output: [3]
