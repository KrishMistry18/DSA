class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):

        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        distance = (closestX - xCenter) ** 2 + (closestY - yCenter) ** 2

        return distance <= radius ** 2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna