class Solution:
    def minSum(self, arr):
        # code here
        n = len(arr)
        arr.sort()
        s1 = s2 = ''
        for i in range(0,n-1,2):
            s1 += str(arr[i])
            s2 += str(arr[i+1])
        if n % 2 :
            s1 += str(arr[-1])
        return self.addNum(s1,s2)
    def addNum(self,s1,s2):
        i,j = len(s1)-1, len(s2)-1
        carry = 0 
        res = []
        
        while i >= 0 or j >= 0 or carry:
            n1 = int(s1[i]) if i >= 0 else 0 
            n2 = int(s2[j]) if j >= 0 else 0 
            total = n1 + n2 + carry
            carry = total // 10
            res.append(str(total % 10))
            
            i -= 1 
            j -= 1 
        return ''.join(res[::-1]).lstrip('0') or '0'