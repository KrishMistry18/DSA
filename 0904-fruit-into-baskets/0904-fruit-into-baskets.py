class Solution(object):
    def totalFruit(self, fruits):
        low = 0
        f = {}
        res = 0

        for high in range(len(fruits)):
            f[fruits[high]] = f.get(fruits[high], 0) + 1

            while len(f) > 2:
                f[fruits[low]] -= 1

                if f[fruits[low]] == 0:
                    del f[fruits[low]]

                low += 1

            res = max(res, high - low + 1)

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna