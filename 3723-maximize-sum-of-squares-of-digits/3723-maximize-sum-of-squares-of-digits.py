class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        result = []

        for i in range(num):
            digit = min(9, sum)
            result.append(str(digit))
            sum -= digit

        if sum > 0:
            return ""

        return ''.join(result)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna