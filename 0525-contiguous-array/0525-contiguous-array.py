class Solution(object):
    def findMaxLength(self, nums):
        zero = 0
        one = 0
        f = {}
        res = 0

        for i in range (len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1

            diff = zero - one
            
            if diff == 0:
                res = max(res, i+1)
            if diff not in f:
                f[diff] = i
            else:
                idx = f[diff]
                l = i - idx
                res = max(l, res)
        
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna