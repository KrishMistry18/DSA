class Solution(object):
    def minPrice(self, prices, discounts):
       
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        sum = 0.0

        for i in range (len(prices)):
            if i < len(discounts):
                sum += prices[i] * (100 - discounts[i]) / 100.0
            else:
                sum += prices[i]

        return sum
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna