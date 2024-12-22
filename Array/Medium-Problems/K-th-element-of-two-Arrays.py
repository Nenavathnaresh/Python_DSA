class Solution:

    def kthElement(self, a, b, k):
        sorted_arr = []
        n = len(a)
        m = len(b)
        i,j = 0, 0
        
        while i < n and j < m:
            if a[i] < b[j]:
                sorted_arr.append(a[i])
                i += 1 
            else:
                sorted_arr.append(b[j])
                j += 1 
        while i < n:
            sorted_arr.append(a[i])
            i += 1 
        while j < m:
            sorted_arr.append(b[j])
            j += 1 
        
        return sorted_arr[k-1]