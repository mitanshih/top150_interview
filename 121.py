
'''121. Best Time to Buy and Sell Stock
Created on 2024-11-28 15:29:16
2024-11-28 15:36:46

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum_price: int = prices[0]
        result: int = 0    # there cannot achieve any profit, return 0.

        for price in prices:
            minimum_price = min(price, minimum_price)
            result = max(result, price - minimum_price)

        return result

        #%%    Main Function

        #%%    Main
if __name__ == '__main__':
    pass

#%%
