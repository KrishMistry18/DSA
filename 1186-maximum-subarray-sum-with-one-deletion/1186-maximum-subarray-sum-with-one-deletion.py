class Solution(object):
    def maximumSum(self, arr):
        no_del = arr[0]
        one_del = 0
        res = arr[0]

        for i in range (1,len(arr)):
            prev_no_del = no_del
            prev_one_del = one_del

            no_del = max(no_del + arr[i], arr[i])
            one_del = max(prev_one_del + arr[i], prev_no_del)

            res = max(res, max(one_del, no_del))
        
        return res




        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna