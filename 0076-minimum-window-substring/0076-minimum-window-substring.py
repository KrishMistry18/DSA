class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        # Frequency of characters in t
        freq = [0] * 128
        for ch in t:
            freq[ord(ch)] += 1

        left = 0
        required = len(t)
        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            # Include current character
            if freq[ord(s[right])] > 0:
                required -= 1
            freq[ord(s[right])] -= 1

            # Try to shrink the window
            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                freq[ord(s[left])] += 1
                if freq[ord(s[left])] > 0:
                    required += 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna