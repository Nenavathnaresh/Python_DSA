def findLongestConseqSubseq(arr, N):
    s = set(arr)
    longest_streak = 0

    for num in s:
        if num - 1 not in s:
            current_num = num
            current_streak = 1

            while current_num + 1 in s:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

arr = [1,4,3,8,9,2]
print(findLongestConseqSubseq(arr,6))