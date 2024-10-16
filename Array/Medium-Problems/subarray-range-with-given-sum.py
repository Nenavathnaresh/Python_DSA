def countSubarraysWithSum(arr, tar):
    # Hash map to store the frequency of cumulative sums
    cumulative_sum_count = {0: 1}
    cumulative_sum = 0
    subarray_count = 0

    for num in arr:
        # Update the cumulative sum
        cumulative_sum += num

        # Check if (cumulative_sum - tar) exists in the map
        if cumulative_sum - tar in cumulative_sum_count:
            subarray_count += cumulative_sum_count[cumulative_sum - tar]

        # Update the cumulative sum count in the map
        if cumulative_sum in cumulative_sum_count:
            cumulative_sum_count[cumulative_sum] += 1
        else:
            cumulative_sum_count[cumulative_sum] = 1

    return subarray_count
