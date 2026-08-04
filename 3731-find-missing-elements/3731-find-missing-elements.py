class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        res = []

        for i in range (nums[0], nums[-1]+1):
            if i not in nums:
                res.append(i)
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna