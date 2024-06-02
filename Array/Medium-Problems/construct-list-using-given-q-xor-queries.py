def constructList(q, queries):
    s = [0]  # Start with the list containing only 0
    cumulative_xor = 0  # To track the cumulative XOR
    
    for query in queries:
        if query[0] == 0:
            # Insert x into the list, adjusted by the cumulative XOR
            s.append(query[1] ^ cumulative_xor)
        elif query[0] == 1:
            # Update the cumulative XOR
            cumulative_xor ^= query[1]
    
    # Apply the final cumulative XOR to each element and sort the list
    s = [a ^ cumulative_xor for a in s]
    s.sort()
    
    return s

# Example usage:
q1 = 5
queries1 = [[0, 6], [0, 3], [0, 2], [1, 4], [1, 5]]
print(constructList(q1, queries1))  # Output: [1, 2, 3, 7]

q2 = 3
queries2 = [[0, 2], [1, 3], [0, 5]]
print(constructList(q2, queries2))  # Output: [1, 3, 5]

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

def constructList(q, queries):
    s = [0]  # Start with the list containing only 0
    
    for query in queries:
        if query[0] == 0:
            # Insert x into the list
            s.append(query[1])
        elif query[0] == 1:
            # Apply XOR x to every element in the list
            x = query[1]
            s = [a ^ x for a in s]
    
    # Sort the list at the end
    s.sort()
    return s

# Example usage:
q1 = 5
queries1 = [[0, 6], [0, 3], [0, 2], [1, 4], [1, 5]]
print(constructList(q1, queries1))  # Output: [1, 2, 3, 7]

q2 = 3
queries2 = [[0, 2], [1, 3], [0, 5]]
print(constructList(q2, queries2))  # Output: [1, 3, 5]
