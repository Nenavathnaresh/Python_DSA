def match_nuts_and_bolts(nuts, bolts):
    # Step 1: Define the required order
    order = ['!', '#', '$', '%', '&', '*', '?', '@', '^']
    
    # Step 2: Create a dictionary to map each character to its position in the order list
    order_dict = {char: i for i, char in enumerate(order)}
    
    # Step 3: Define a sorting function that uses the order dictionary
    def sort_key(char):
        return order_dict[char]
    
    # Step 4: Sort both nuts and bolts arrays using the sorting function
    nuts.sort(key=sort_key)
    bolts.sort(key=sort_key)
    
    # Step 5: Return the sorted arrays (optional, since they are modified in-place)
    return nuts, bolts

# Test the function with given test cases
nuts1 = ['@', '%', '$', '#', '^']
bolts1 = ['%', '@', '#', '$', '^']
nuts2 = ['^', '&', '%', '@', '#', '*', '$', '?', '!']
bolts2 = ['?', '#', '@', '%', '&', '*', '$', '^', '!']

matched_nuts1, matched_bolts1 = match_nuts_and_bolts(nuts1, bolts1)
matched_nuts2, matched_bolts2 = match_nuts_and_bolts(nuts2, bolts2)

# Print the results
print("Matched nuts and bolts set 1:")
print("Nuts: ", matched_nuts1)
print("Bolts:", matched_bolts1)

print("Matched nuts and bolts set 2:")
print("Nuts: ", matched_nuts2)
print("Bolts:", matched_bolts2)
