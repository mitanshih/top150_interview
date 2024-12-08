
'''15. 3Sum
Created on 2024-12-06 17:28:55
2024-12-06 18:03:17

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        limit: int = len(nums) - 1

        result: list[list[int]] = []

        for index, value in enumerate(nums):
            if value > 0:
                break    # sum(`value`, `nums[left]`, `nums[right]`) always > 0
            if (index > 0) and value == nums[index - 1]:
                continue
            left, right = index + 1, limit    #two-pointer
            while left < right:
                amount: int = value + nums[left] + nums[right]
                if amount == 0:
                    result.append([value, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while nums[left - 1] == nums[left] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1

                elif amount < 0:
                    left += 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1
                else:
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1

        return result


#%%    Main Function
Solution().threeSum([0, 0, 0])

#%%    Main
if __name__ == '__main__':
    pass

#%%
