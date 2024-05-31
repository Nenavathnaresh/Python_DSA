# &&&&&&&&&&&&&&&&&&&&&&&& Backtracking method &&&&&&&&&&&&&&&&&&&&&&&

class Solution:
    def solve(self, ind, a, k, n, v, ans):
        if k == 0:
            ans.append(v[:])
            return 
        if ind == n or k < 0:
            return 
        for i in range(ind, n):
            if i != ind and a[i] == a[i-1]:
                continue
            v.append(a[i])
            self.solve(i+1, a, k-a[i], n, v, ans)
            v.pop()
    
    def CombinationSum2(self, arr, n, k):
        # code here
        arr.sort()
        v = []
        ans = []
        self.solve(0, arr, k, len(arr), v, ans)
        return ans
        # result = []
        # def backtrack(start, target, path):
        #     if target == 0:
        #         result.append(path)
        #         return 
        #     for i in range(start, n):
                
        #         if target < arr[i]:
        #             break
        #         if i < start and arr[i] == arr[i-1]:
        #             continue
        #         backtrack(i+1, target - arr[i], path+[arr[i]])
        # backtrack(0, k, [])
        # return result