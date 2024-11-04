class Solution:

    def countTriplet(self, arr):
        # Sorting the array in ascending order.
        n = len(arr)
        arr.sort()

        # Initializing the count of triplets as 0.
        ans = 0

        # Iterating over the array in reverse order.
        for i in range(n - 1, -1, -1):

            # Initializing two pointers, one at the beginning and one at i-1.
            j = 0
            k = i - 1

            # Using two-pointer approach to find the triplets.
            while j < k:
                # If the given condition is satisfied, increment the count and move the pointers.
                if arr[i] == arr[j] + arr[k]:
                    ans += 1
                    j += 1
                    k -= 1
                # If the sum is less than the target, move the left pointer.
                elif arr[i] > arr[j] + arr[k]:
                    j += 1
                # If the sum is greater than the target, move the right pointer.
                else:
                    k -= 1

        # Returning the count of triplets.
        return ans