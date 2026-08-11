class Solution(object):
    def isValid(self, s):
        stack = []

        for ch in s:

            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            else:
                if not stack:
                    return False

                top = stack[-1]

                if ch == ')' and top != '(':
                    return False

                if ch == '}' and top != '{':
                    return False

                if ch == ']' and top != '[':
                    return False

                stack.pop()

        return not stack

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna