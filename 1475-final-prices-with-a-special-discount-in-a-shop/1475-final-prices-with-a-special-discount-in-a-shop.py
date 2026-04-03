class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = prices[:]
        stack = []

        for i in range(0, len(prices)):

            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                output[idx] = prices[idx] - prices[i]

            stack.append(i)

        return output
