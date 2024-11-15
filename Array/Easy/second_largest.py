def find_second_largest(arr):
    first, second = -1, -1
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num < first and num > second:
            second = num
            
    return second if second != -1 else -1
