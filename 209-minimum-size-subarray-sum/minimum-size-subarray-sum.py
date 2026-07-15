class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        low = 0
        l = 0
        high = 0
        sum = 0
        res = float('inf')

        while high < n:
            sum = sum + nums[high]

            while sum >= target:
                l = high - low + 1
                res = min(l,res)

                sum = sum - nums[low]
                low += 1

            high += 1

        if res == float('inf'):
            return 0
        else:
            return res