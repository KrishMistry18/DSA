class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        curr = ""

        for ch in s:
            if ch == '(':
                stack.append(curr)
                curr = ""

            elif ch == ')':
                curr = curr[::-1]
                curr = stack.pop() + curr

            else:
                curr += ch

        return curr

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna