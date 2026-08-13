class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        answer = [0] * len(temperatures)

        for i in range (len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                answer[index] = i - index 
            
            stack.append(i)

        return answer


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna