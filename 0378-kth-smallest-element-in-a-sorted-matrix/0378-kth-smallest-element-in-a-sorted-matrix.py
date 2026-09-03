class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        m = len(matrix[0])

        low = matrix[0][0]
        high = matrix[n - 1][m - 1]

        while low <= high:
            guess = (low + high) // 2
            ans = self.fun(matrix, n, m, guess)

            if ans < k:
                low = guess + 1
            else:
                high = guess - 1
                res = guess

        return res

    def fun(self, matrix, n, m, target):
        row = n - 1
        col = 0
        count = 0

        while row >= 0 and col < m:
            if matrix[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna