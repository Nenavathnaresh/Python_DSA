class Solution:

    def findTriplets(self, arr):
        # Set to handle duplicates
        res_set = set()
        n = len(arr)
        mp = {}

        # Store sum of all the pairs with their indices
        for i in range(n):
            for j in range(i + 1, n):
                pair_sum = arr[i] + arr[j]
                if pair_sum not in mp:
                    mp[pair_sum] = []
                mp[pair_sum].append((i, j))

        for i in range(n):
            # Find remaining value to get zero sum
            rem = -arr[i]
            if rem in mp:
                pairs = mp[rem]
                for p in pairs:
                    # Ensure no two indices are same in triplet
                    if p[0] != i and p[1] != i:
                        curr = tuple(sorted([i, p[0], p[1]]))
                        res_set.add(curr)

        return [list(triplet) for triplet in res_set]