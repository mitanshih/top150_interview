
'''11. Container With Most Water
Created on 2024-12-02 23:09:05
2024-12-02 23:50:34

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions


#%%    Main Function
class Solution:
    def maxArea(self, height: list[int]) -> int:
        result: int = 0
        left, right = 0, len(height) - 1    #two-pointer

        # The biggest answer is more likely to appear
        # where the two lines are furthest apart.
        # Therefore, there may be redundant calculations
        # when `left` and `right` are almost close to the middle.
        height_maximum: int = max(height)

        while left < right:
            result = max(
                #formula for the amount of water that a container can store
                min(height[left], height[right]) * (right - left),
                result
            )
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            if height_maximum * (right - left) < result:
                break    # Early break when `result` is never bigger.

        return result


#%%    Main
if __name__ == '__main__':
    pass

#%%
