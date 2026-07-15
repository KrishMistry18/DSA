class Solution(object):
    def twoSum(self, nums, target):
        arr = [(nums[i], i) for i in range(len(nums))]
        arr.sort()

        i = 0
        j = len(arr) - 1

        while i < j:
            current_sum = arr[i][0] + arr[j][0]

            if current_sum == target:
                return [arr[i][1], arr[j][1]]
            elif current_sum < target:
                i += 1
            else:
                j -= 1