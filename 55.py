
'''55. Jump Game
Created on 2024-11-29 14:20:09
2024-11-29 14:59:46

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def canJump(self, nums: list[int]) -> bool:
        target: int = len(nums) - 1

        # Update `target` *from the bottom* which can reach.
        for current in range(len(nums) - 2, -1, -1):
            if current + nums[current] >= target:
                target = current

        return target == 0    # Can `target` reach the head?


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        terminal: int = len(nums) - 1

        current: int = 0
        went_index: set[int] = {current, }    #initial position

        steps: list[int] = [current]
        while steps:
            current = steps.pop()
            if current >= terminal:    # `current` can reach the last index!
                return True
            for index in range(current + 1, current + 1 + nums[current]):
                if index in went_index:
                    continue
                steps.append(index)
                went_index.add(index)

        return False    # It is impossible to reach the last index.


#%%    Main Function
Solution().canJump([2, 0])

#%%    Main
if __name__ == '__main__':
    pass

#%%
