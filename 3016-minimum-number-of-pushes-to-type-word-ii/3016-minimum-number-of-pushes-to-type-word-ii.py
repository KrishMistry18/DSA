class Solution(object):
    def minimumPushes(self, word):
        f = {}
        res = 0

        for ch in word:
            f[ch] = f.get(ch, 0) + 1

        count = len(f)

        while count > 0:          
            mini = min(f.values())

            for ch in f:
                if f[ch] == mini:
                    key = ch
                    break

            if count <= 8:
                res += mini * 1
            elif count <= 16:
                res += mini * 2
            elif count <= 24:
                res += mini * 3
            else:
                res += mini * 4

            del f[key]
            count -= 1

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna