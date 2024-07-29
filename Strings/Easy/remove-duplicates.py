# class Solution:
# 	def removeDups(str):
# 		dit = {}
# 		s = ''
# 		for char in str:
# 		    if char in dit:
# 		        dit[char] = 1
# 		    else:
# 		        s += char
# 		        dit[char] = 1
# 	    return s

def removeDuplicates(s: str) -> str:
    # Initialize a set to track seen characters
    seen = set()
    # Initialize an empty list to build the result
    result = []
    
    # Iterate over each character in the string
    for char in s:
        # If character is not seen before
        if char not in seen:
            # Add it to the set
            seen.add(char)
            # Append it to the result
            result.append(char)
    
    # Join the result list to form the final string
    return ''.join(result)

# Example usage
print(removeDuplicates("zvvo"))  # Output: "zvo"
print(removeDuplicates("gfg"))   # Output: "gf"
