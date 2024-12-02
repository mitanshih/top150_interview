
'''167. Two Sum II - Input Array Is Sorted
Created on 2024-12-02 22:19:37
2024-12-02 22:36:54

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1    #two-pointer

        while left < right:
            answer: int = numbers[left] + numbers[right]
            if answer < target:
                left += 1
            elif answer > target:
                right -= 1
            else:
                left += 1   #1-indexed
                right += 1  #1-indexed
                break    #match!

        return [left, right]

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
