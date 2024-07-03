class Solution:
    def shuffleArray(self, arr, n):
        i = n // 2 - 1
        for j in range(n-1, n//2 - 1, -1):
            arr[j] <<= 10
            arr[j] |= arr[i]
            i -= 1

        i = 0
        for j in range(n // 2, n):
            num1 = arr[j] & 1023
            num2 = arr[j] >> 10
            arr[i] = num1
            arr[i + 1] = num2
            i += 2

# Example usage
solution = Solution()

arr1 = [1, 2, 9, 15]
n1 = len(arr1)
solution.shuffleArray(arr1, n1)
print(arr1)  # Output: [1, 9, 2, 15]

arr2 = [1, 2, 3, 4, 5, 6]
n2 = len(arr2)
solution.shuffleArray(arr2, n2)
print(arr2)  # Output: [1, 4, 2, 5, 3, 6]
