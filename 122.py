
'''122. Best Time to Buy and Sell Stock II
Created on 2024-11-28 15:58:46
2024-11-28 17:11:22

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def maxProfit(self, prices: list[int]) -> int:
        low_price: int = prices[0]

        result: int = 0
        for num in prices[1:]:

            if num <= low_price:
                low_price = num
            else:
                result += num - low_price
                low_price = num

        return result

# The biggest difference between the reference submission and mine
# is that the reference's selling timing is every time the stock rises;
# however, my selling timing is every time the stock falls.

# We all want stocks to go as high as possible.
# Therefore, my submission can reduce the handling fees
# in the rising stocks by minimizing the number of transactions.

# However, if you consider code maintainability and logic clarity,
# I think the reference submission is still better.


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 3:    # Is there a profit?
            return (0 if len(prices) == 1 or prices[1] < prices[0]
                    else prices[1] - prices[0])

        # Searching the increasing stock...
        is_increasing_index: int = 1
        while is_increasing_index < len(prices) - 1:
            if prices[is_increasing_index - 1] < prices[is_increasing_index]:
                break
            is_increasing_index += 1

        # To sell the stock when it decreases, and buy it.
        result: int = 0    # There cannot achieve any profit, return 0.
        low_price: int = prices[is_increasing_index - 1]    #buy stock

        for previous_index, price in enumerate(prices[is_increasing_index:],
                                               is_increasing_index - 1):
            if price < prices[previous_index]:    # Does it decrease?
                result += prices[previous_index] - low_price    #sell stock
                low_price = price    #buy stock

        if price > low_price:    # Can there achieve the last transactions?
            return result + price - low_price
        return result


#%%    Main Function
Solution().maxProfit([2, 1, 4])

#%%    Main
if __name__ == '__main__':
    pass

#%%
