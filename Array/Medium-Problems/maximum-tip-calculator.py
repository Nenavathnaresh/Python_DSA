def maximize_tips(n, x, y, arr, brr):
    # Step 1: Create a list of tuples where each tuple contains (tip difference, A's tip, B's tip)
    orders = [(abs(arr[i] - brr[i]), arr[i], brr[i]) for i in range(n)]
    
    # Step 2: Sort the list based on the absolute difference in descending order
    orders.sort(reverse=True, key=lambda x: x[0])
    
    # Initialize total tips and counters for A and B
    total_tips = 0
    a_count = 0
    b_count = 0
    
    # Step 3: Assign orders to maximize tips
    for diff, a_tip, b_tip in orders:
        if (a_tip >= b_tip and a_count < x) or b_count >= y:
            # Assign to A if A's tip is greater or equal and A can take more orders, or if B is full
            total_tips += a_tip
            a_count += 1
        else:
            # Assign to B otherwise
            total_tips += b_tip
            b_count += 1
    
    return total_tips

# Test cases
print(maximize_tips(5, 3, 3, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1])) # Expected output: 21
print(maximize_tips(8, 4, 4, [1, 4, 3, 2, 7, 5, 9, 6], [1, 2, 3, 6, 5, 4, 9, 8])) # Expected output: 43
print(maximize_tips(7, 3, 4, [8, 7, 15, 19, 16, 16, 18], [1, 7, 15, 11, 12, 31, 9])) # Expected output: 110
