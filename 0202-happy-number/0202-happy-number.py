class Solution(object):
    def isHappy(self, n):
        def fun(n):
            sum = 0
            while n > 0:
                d = n % 10
                n //= 10
                sum += d * d
            return sum

        slow = n
        fast = n

        while True:
            slow = fun(slow)

            fast = fun(fast)
            fast = fun(fast)

            if fast == 1:
                return True

            if slow == fast:
                return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna