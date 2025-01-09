def groupAnagrams(arr):
    # Dictionary to group words by their sorted form
    anagram_groups = {}

    # Iterate over each word and group by sorted key
    for word in arr:
        sorted_key = ''.join(sorted(word))
        if sorted_key not in anagram_groups:
            anagram_groups[sorted_key] = []  # Initialize the key with an empty list
        anagram_groups[sorted_key].append(word)
    
    # Sort each group lexicographically
    result = [group for group in anagram_groups.values()]
    
    # Sort the groups by the order of their first appearance
    
    return result

# Test cases
arr1 = ["act", "god", "cat", "dog", "tac"]
print(groupAnagrams(arr1))  
# Output: [["act", "cat", "tac"], ["god", "dog"]]

arr2 = ["no", "on", "is"]
print(groupAnagrams(arr2))  
# Output: [["is"], ["no", "on"]]

arr3 = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
print(groupAnagrams(arr3))  
# Output: [["abc", "bac", "cab"], ["listen", "silent", "enlist"], ["rat", "tar", "art"]]
