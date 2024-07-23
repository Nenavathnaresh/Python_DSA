class Solution:
    
    # Function to check if it is possible to achieve the target X
    
    def isPossible(self, S, N, X, A):
        
        sum=S
        a=[]
        a.append(S)

        # calculating the cumulative sum and storing in 'a'
        for i in range(N):
            a.append(sum+A[i])
            sum+=a[-1]
            a.sort

        # iterating through 'a' in reverse order
        for i in range(len(a)-1,-1,-1):
            # if the current value is greater than or equal to X, skip to the next iteration
            if a[i]>X:
                continue
            else:
                X-=a[i]
                # if X becomes 0, return True
                if X==0:
                    return True

        # if no possible distribution is found, return False
        return False