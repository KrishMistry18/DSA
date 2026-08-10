class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        res = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):

            start1 = firstList[i][0]
            end1 = firstList[i][1]

            start2 = secondList[j][0]
            end2 = secondList[j][1]

            s = max(start1, start2)
            e = min(end1, end2)

            if s <= e:
                res.append([s, e])

            if end1 <= end2:
                i += 1
            else:
                j += 1

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna