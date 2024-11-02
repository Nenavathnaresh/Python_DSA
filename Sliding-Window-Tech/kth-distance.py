def contains_duplicates_within_k(arr, k):
    # Set to store elements within the current window of size k
    seen = set()
    
    for i in range(len(arr)):
        # Check if current element is already in the set
        if arr[i] in seen:
            return True  # Duplicate found within k distance
        
        # Add the current element to the set
        seen.add(arr[i])
        
        # Maintain the window size to k by removing the element that goes out of the window
        if i >= k:
            seen.remove(arr[i - k])
    
    return False  # No duplicates found within k distance
