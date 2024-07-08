class Solution:
    def shiftPile(self, N, n):
        # create an empty array to store the movements
        arr=[]
        
        # recursive function to solve the problem
        self.solve('1','2','3',N,arr)
        
        # return the nth movement from the array
        return arr[n-1]

    def solve(self,src,temp,dest,N,arr):
        # base case: if N is 0, then there are no discs to move
        if N==0:
            return
        
        # recursive calls to move the discs
        self.solve(src,dest,temp,N-1,arr)
        
        # append the movement of top disc from src to dest in the array
        arr.append([src,dest])
        
        # recursive call to move the remaining discs from temp to dest
        self.solve(temp,src,dest,N-1,arr)