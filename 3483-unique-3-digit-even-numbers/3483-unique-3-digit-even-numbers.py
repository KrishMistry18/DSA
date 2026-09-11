class Solution(object):
    def totalNumbers(self, digits):

        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        ans = 0

        for a in range(1, 10):       # hundreds
            for b in range(10):      # tens
                for c in range(0, 10, 2):  # units: even

                    # Use a copy so we can "use" digits
                    temp = freq[:]

                    temp[a] -= 1
                    temp[b] -= 1
                    temp[c] -= 1

                    if temp[a] >= 0 and temp[b] >= 0 and temp[c] >= 0:
                        ans += 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna