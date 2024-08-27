class Solution:

    def dfs(self, parent, ans, connectChars):
        ans[parent] = 1
        for i in connectChars[parent]:
            if not ans[i]:
                self.dfs(i, ans, connectChars)

    def binaryPalindrome(self, n, k):
        arr = [i % k for i in range(n)]
        ans = [0] * n
        connectChars = [[] for _ in range(k)]

        # Connect characters in the connectChars array
        for i in range(n):
            connectChars[arr[i]].append(arr[n - i - 1])
            connectChars[arr[n - i - 1]].append(arr[i])

        # Run dfs on the connected characters to mark them with 1 in the ans array
        self.dfs(0, ans, connectChars)

        # Create the binary palindrome string using the ans array
        s = "".join(["1" if ans[arr[i]] == 1 else "0" for i in range(n)])

        # Return the binary palindrome string
        return s