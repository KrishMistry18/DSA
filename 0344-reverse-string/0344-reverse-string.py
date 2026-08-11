class Solution(object):
    def reverseString(self, s):
        stack = []
        
        for i in range(len(s)):
            stack.append(s[i])

        for i in range(len(s)):
            s[i] = stack.pop()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna