def pattern(n):
    def decrease(n):
        if n <= 0:
            return [n]
        return [n] + decrease(n - 5)
    
    def increase(n, original):
        if n == original:
            return [n]
        return [n] + increase(n + 5, original)
    
    # Get the decreasing part including the point where it becomes less than or equal to 0
    decreasing_part = decrease(n)
    # Get the increasing part from the element that is just after the last in decreasing part
    increasing_part = increase(decreasing_part[-1], n)
    
    # Combine both parts
    return decreasing_part + increasing_part[1:]

# Example usage:
print(pattern(16))  # Output: [16, 11, 6, 1, -4, 1, 6, 11, 16]
print(pattern(10))  # Output: [10, 5, 0, 5, 10]



# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def pattern(n):
    result = []
    current = n
    # Decreasing phase
    while current > 0:
        result.append(current)
        current -= 5
    
    # Adding the last non-positive number
    result.append(current)
    
    # Increasing phase
    while current < n:
        current += 5
        result.append(current)
    
    return result

# Example usage:
print(pattern(16))  # Output: [16, 11, 6, 1, -4, 1, 6, 11, 16]
print(pattern(10))  # Output: [10, 5, 0, 5, 10]
print(pattern(13074))  # Test with a large number to ensure it works correctly
