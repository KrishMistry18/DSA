class Solution(object):
    def subsets(self, nums):
        subset = [[]]

        for num in nums:
            n = len(subset)
            for i in range(n):
                subset.append(subset[i] + [num])

        return subset

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna