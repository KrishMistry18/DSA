class Solution(object):

  def plusOne(self, digits):
    n = len(digits)
    high = n - 1

    if digits[high] == 9:

      for i in range(high, -1, -1):
        if digits[i] < 9:
          digits[i] += 1
          return digits
        digits[i] = 0

      return [1] + digits

    digits[high] += 1
    return digits

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna