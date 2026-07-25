class Solution(object):

  def plusOne(self, digits):
    n = len(digits)
    temp = 0

    for digit in digits:
      temp = temp * 10 + digit

    temp = temp + 1
    digits = []
    
    while temp > 0:
      digits.append(temp % 10)
      temp = temp // 10

    digits = digits[::-1]

    return digits

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna