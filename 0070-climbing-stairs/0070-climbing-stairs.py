class Solution(object):
    def climbStairs(self, n):
        if n <= 3:
            return n

        a = 2
        b = 3 

        for i in range (4,n + 1):
            c = a + b
            a = b
            b = c

        return b         

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna