class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x!= 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        rev *= sign

        if rev < INT_MIN or rev > INT_MAX:
            return 0

        return rev

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna