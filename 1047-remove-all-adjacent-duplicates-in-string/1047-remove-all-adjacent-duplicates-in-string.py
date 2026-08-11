class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        
        for letter in s:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)

        return "".join(stack)





   



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna