class Solution(object):
    def maxNumberOfBalloons(self, text):
        have = {}
        need = {}
        res = float('inf')

        for i in range (len(text)):
            have[text[i]] = have.get(text[i], 0) + 1

        need['b'] = 1
        need['a'] = 1
        need['l'] = 2
        need['o'] = 2
        need['n'] = 1

        for char in need:
            if char not in have:
                return 0

            times = have[char] // need[char]
            res = min(res,times)

        return res

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna