class Solution(object):
    def swapPairs(self, head):
        left = head
        res = None
        prev_left = None
        size = 2

        while left:
            right = left

            for i in range(size - 1):
                if right == None:
                    break
                    
                right = right.next

            if right == None:
                if prev_left:
                    prev_left.next = left
                else:
                    res = left
                break

            next_left = right.next
            prev = None
            curr = left

            for i in range(size):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            if prev_left:
                prev_left.next = right
            else:
                res = right

            prev_left = left
            left = next_left

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna