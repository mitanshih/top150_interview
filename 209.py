
'''209. Minimum Size Subarray Sum
Created on 2024-12-08 14:58:57
2024-12-08 17:00:14

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_single_loop:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left: int = 0
        right: int = 1

        limit: int = len(nums)

        amount: int = nums[0]
        result: int = float('inf')  # type: ignore
        while right <= limit:    # Last iteration checks the further `left`.
            if amount < target:
                if right < limit:
                    amount += nums[right]

                right += 1
            else:
                result = min(result, right - left)
                amount -= nums[left]

                left += 1

        return 0 if result == float('inf') else result


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        amount: int = 0
        sliding_left: int = 0

        result: int = float('inf')  # type: ignore
        for index, num in enumerate(nums, 1):
            amount += num
            while amount >= target:
                amount -= nums[sliding_left]
                result = min(index - sliding_left, result)

                sliding_left += 1

        return 0 if result == float('inf') else result


#%%    Main Function
Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])

#%%    Main
if __name__ == '__main__':
    pass

#%%
