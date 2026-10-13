class Solution(object):
    def maxAlternatingSum(self, nums):
        squares = sorted((x * x for x in nums), reverse=True)

        positive_count = (len(nums) + 1) // 2

        return sum(squares[:positive_count]) - sum(squares[positive_count:])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna