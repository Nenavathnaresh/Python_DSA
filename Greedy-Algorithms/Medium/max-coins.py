from bisect import bisect_left


class Solution:
    def maxCoins(n,ranges):
        #Sorting the ranges based on their end points 
        ranges.sort(key=lambda x:(x[1],x[0]))
        
        #Initializing variables
        temp=[-1]
        d={}
        d[-1]=0
        ans=0   
        prev=0
        
        #Iterating over the ranges
        for i in range(n):
            #Updating the maximum answer
            ans=max(ans,ranges[i][2])
            
            #Finding the index of the start point in the temp list
            ind=bisect_left(temp,ranges[i][0])
            
            #Checking if the start point is not found and adjusting the index
            if ind>=len(temp) or ranges[i][0]<temp[ind]:
                ind-=1
            
            #Updating the maximum answer by considering the current range and the previous maximum answer
            ans=max(ans,ranges[i][2]+d[temp[ind]])
            
            #Updating the maximum answer for the current end point
            d[ranges[i][1]]=max(prev,ranges[i][2])
            
            #Adding the current end point to the temp list
            temp.append(ranges[i][1])
            
            #Updating the previous maximum answer
            prev=max(prev,ranges[i][2])
        
        #Returning the maximum answer
        return ans
        
        # Example usage:
    n1 = 3
    ranges1 = [[1, 3, 4], [2, 3, 5], [3, 4, 2]]
    print(maxCoins(n1, ranges1))  # Output: 7

    n2 = 5
    ranges2 = [[1, 3, 4], [2, 3, 5], [3, 4, 2], [5, 8, 9], [2, 8, 10]]
    print(maxCoins(n2, ranges2))  # Output: 14