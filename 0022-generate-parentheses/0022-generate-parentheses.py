class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(path, open, close):
            if len(path) == 2 * n:
                result.append(''.join(path))
                return

            if open < n:
                path.append('(')
                backtrack(path, open + 1, close)
                path.pop()

            if close < open:
                path.append(')')
                backtrack(path, open, close + 1)
                path.pop()

        backtrack([], 0, 0)

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna