class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = n * m - 1

        while low <= high:
            guess = (high + low)//2
            row = guess // m
            col = guess % m

            if matrix[row][col] == target:
                return True

            if matrix[row][col] < target:
                low = guess + 1

            else:
                high = guess - 1

        return False

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna