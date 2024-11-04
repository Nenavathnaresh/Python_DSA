from collections import deque

def firstNonRepeating(s):
    # Initialize frequency array for 26 lowercase letters
    freq = [0] * 26
    # Queue to track the order of characters that could be non-repeating
    queue = deque()
    # Result to store the answer
    result = []
    
    for c in s:
        # Update the frequency of the current character
        index = ord(c) - ord('a')
        freq[index] += 1
        
        # Add character to the queue if it's the first time we encounter it
        if freq[index] == 1:
            queue.append(c)
        
        # Remove characters from the front of the queue if they are repeating
        while queue and freq[ord(queue[0]) - ord('a')] > 1:
            queue.popleft()
        
        # Append the first non-repeating character or '#' if none exist
        if queue:
            result.append(queue[0])
        else:
            result.append('#')
    
    # Join the result list into a single string and return
    return ''.join(result)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5



# def FirstNonRepeatings(s):
#     from collections import deque

#     freq = {}
# 	queue = deque()
# 	res = []
		
# 	for char in s:
# 		freq[char] = freq.get(char,0)+1
		    
# 		if freq[char] == 1:
# 		    queue.append(char)
		    
# 		while queue and freq[queue[0]] > 1:
# 		    queue.popleft()
		    
# 		if queue:
# 		    res.append(queue[0])
# 		else:
# 		    res.append('#')
	
# 	return ''.join(res)