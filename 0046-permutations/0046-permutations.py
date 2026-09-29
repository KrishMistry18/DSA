class Solution(object):
  def permute(self, nums):
    res = []

    def backtrack(path, visited):
      if len(path) == len(nums):
        res.append(list(path))
        return

      for num in nums:
        if num not in visited:
          visited.add(num)
          path.append(num)
          backtrack(path, visited)
          path.pop()
          visited.remove(num)

    backtrack([], set())
    return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna