def count_rectangles_in_circle(r):
    count = 0
    limit = 2 * r
    
    for l in range(1, limit + 1):
        for w in range(1, limit + 1):
            if l * l + w * w <= 4 * r * r:
                count += 1
                
    return count

# Example usage:
print(count_rectangles_in_circle(1))  # Output: 1
print(count_rectangles_in_circle(2))  # Output: 8
print(count_rectangles_in_circle(5))  # Example with a larger radius
