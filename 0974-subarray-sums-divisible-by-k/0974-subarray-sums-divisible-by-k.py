class Solution(object):
    def subarraysDivByK(self, nums, k):
        f = {}
        sum = 0 
        f[0] = 1
        count = 0

        for i in range(len(nums)):
            sum += nums[i]

            rem = sum % k
            if rem < 0:
                rem = rem + k

            count += f.get(rem, 0)
            f[rem] = f.get(rem, 0) + 1

        return count


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna