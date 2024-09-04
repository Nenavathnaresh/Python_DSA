class Solution:
    def wordBreak(self, n, s, dictionary):
    
        # create a dictionary to store words from the dictionary list
        dic = {}
    
        # iterate through the words in the dictionary list
        for i in  dictionary:
    
            # check if the word exists in the input s
            if i in s:
    
                # if the first letter of the word exists in the dictionary 
                # dictionary, append the word to the list associated with 
                # that letter; otherwise, create a new list with the word
                if i[0] in dic:
                    dic[i[0]].append(i)
                else:
                    dic[i[0]]=[i]
        
        # define a recursive function to solve the word break problem
        def solve(st, k,  dp):
    
            # base case: if the entire string is broken
            if len(st)==k:
                return True
            
            # if the current substring has already been processed,
            # return its corresponding result
            elif  dp[k]!=None:
                return  dp[k]
            
            # if the current character has associated words in the dictionary
            elif st[k] in dic:
    
                # iterate through the words associated with the current 
                # character in the dictionary
                for i in dic[st[k]]:
    
                    # check if the length of the word is smaller or equal 
                    # to the remaining substring
                    if len(i)<=len(st[k:]):
    
                        # check if the word matches the current substring
                        if st[k:k+len(i)]==i:
    
                            # increment k by the length of the matched word
                            k+=len(i)
                            
                            # recursively call the solve function with the 
                            # updated substring
                            rt = solve(st,k, dp)
    
                            # if the recursive call returns True, update 
                            # the corresponding result and return True
                            if rt:
                                dp[k]=True
                                return True
                            else:
    
                                # if the recursive call returns False, 
                                # decrement k by the length of the matched 
                                # word to backtrack
                                k=k-len(i)
    
                # if none of the words match the current substring, update 
                # the result to False and return False
                dp[k]=False
                return False     
            else:
    
                # if the current character does not have associated words 
                # in the dictionary, update the result to False and return False
                dp[k]=False
                return False
    
        # initialize a list to store the results of the solve function 
        dp=[None]*(len(s)+1)
    
        # set the initial value of k to 0
        k=0
    
        # call the solve function to check if it is possible to break the string
        res = solve(s, k,  dp)
    
        # return the final result
        return res
    
    #################################################################################################



def wordBreak(n, s, dictionary):
    # Convert the dictionary list to a set for O(1) lookup times
    word_set = set(dictionary)
    
    # DP array of length len(s) + 1
    dp = [False] * (len(s) + 1)
    
    # Base case: an empty string can always be segmented
    dp[0] = True
    
    # Fill the DP array
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    # The final value dp[len(s)] will tell us if we can segment the entire string
    return 1 if dp[len(s)] else 0

# Example usage:
n = 6
s = "ilikesamsung"
dictionary = ["i", "like", "sam", "sung", "samsung", "mobile"]

print(wordBreak(n, s, dictionary))  # Output: 1
