class Solution(object):
    def maxProduct(self, nums):
        i = 0
        j = 0

        for num in nums:
            if num > i:
                j = i
                i = num
            elif num > j:
                j = num

        return (i - 1) * (j - 1)


    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna