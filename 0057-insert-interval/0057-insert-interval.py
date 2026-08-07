class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        insert = False

        for interval in intervals:
            if not insert and newInterval[0] < interval[0]:
                res.append(newInterval)
                insert = True
            res.append(interval)

        if not insert:
            res.append(newInterval)

        ans = []
        start1 = res[0][0]
        end1 = res[0][1]

        for i in range(1, len(res)):
            start2 = res[i][0]
            end2 = res[i][1]

            if end1 >= start2:
                end1 = max(end1, end2)
            else:
                ans.append([start1, end1])
                start1 = start2
                end1 = end2

        ans.append([start1, end1])
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna