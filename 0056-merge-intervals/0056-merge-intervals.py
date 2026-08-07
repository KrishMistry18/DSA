class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res=[]
        start1 = intervals[0] [0]
        end1 = intervals[0] [1]
        for i in range (1,len(intervals)):
            start2 = intervals[i] [0]
            end2 = intervals[i] [1]

            if end1 >= start2:
                start1 = start1
                end1 = max(end1, end2)
            else:
                res.append([start1, end1])
                start1 = start2
                end1 = end2

        res.append([start1, end1])
        return res




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna