class Solution(object):
    def minEatingSpeed(self, piles, h):

        def fun(speed):
            hours = 0

            for pile in piles:
                hours += pile // speed

                if pile % speed != 0:
                    hours += 1

            return hours

        low = 1
        high = max(piles)
        res = -1

        while low <= high:
            guess = (low + high) // 2

            hours = fun(guess)

            if hours > h:
                low = guess + 1
            else:
                res = guess
                high = guess - 1

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna