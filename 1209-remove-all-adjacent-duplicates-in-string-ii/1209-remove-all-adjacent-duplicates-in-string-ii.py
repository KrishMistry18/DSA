class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []

        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1

                if stack[-1][1] == k:
                    stack.pop()

        res = ""

        while stack:
            c, count = stack.pop()
            res = c * count + res

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna