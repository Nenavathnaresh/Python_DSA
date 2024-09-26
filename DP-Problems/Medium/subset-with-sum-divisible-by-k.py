class Solution:

    def DivisibleByM(self, arr, k):
        n = len(arr)
        if n > k:
            return 1

        # This array will keep track of all the possible sums (after modulo k)
        # which can be made using subsets of arr[]
        # initializing boolean array with all False
        DP = [False] * k

        # We'll loop through all the elements of arr[]
        for i in range(n):
            # anytime we encounter a sum divisible by k, we are done
            if DP[0]:
                return 1

            # To store all the new encountered sums (after modulo).
            # It is used to make sure that arr[i] is added only to
            # those entries for which DP[j] was true before the current iteration.
            temp = [False] * k

            # For each element of arr[], we loop through all elements of DP table
            # from 0 to k-1 and we add the current element, i.e., arr[i], to
            # all those elements which are true in DP table
            for j in range(k):
                # if an element is true in DP table
                if DP[j]:
                    if not DP[(j + arr[i]) % k]:
                        # We update it in temp and update DP once the loop of j is over
                        temp[(j + arr[i]) % k] = True

            # Updating all the elements of temp to DP table since iteration over j is over
            for j in range(k):
                if temp[j]:
                    DP[j] = True

            # Also, since arr[i] is a single element subset, arr[i] % k is one of the possible sums
            DP[arr[i] % k] = True

        return 1 if DP[0] else 0