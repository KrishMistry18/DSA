class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])

        row = n - 1
        col = 0

        while row >= 0 and col < m:
            if matrix[row][col] == target:
                return True

            if matrix[row][col] > target:
                row -= 1

            else:
                col += 1

        return False
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna