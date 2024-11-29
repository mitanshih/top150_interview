
'''45. Jump Game II
Created on 2024-11-29 15:31:36
2024-11-29 16:57:29

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        terminal: int = len(nums) - 1
        # record of current coverage, record of last jump index
        coverage, last_jump_index = 0, 0

        result: int = 0
        # Greedy strategy: extend coverage as long as possible with lazy jump
        for index in range(len(nums)):
            # `coverage` extends as further as possible.
            coverage = max(coverage, index + nums[index])

            if index == last_jump_index:    #forced to jump to extend coverage
                last_jump_index = coverage    #update last jump index
                result += 1    #update counter of jump
                # Check if reached destination already.
                if coverage >= terminal:
                    return result

        return result


class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        indexes: list[int] = []
        terminal: int = len(nums) - 1

        current: int = 0
        went_index: set[int] = {current, }    #initial position

        steps: list[int] = [current]
        temp: dict[int, int] = {}
        while steps:
            current = steps.pop()
            #if current >= terminal:    # Can `current` reach the last index?
            #    break

            # `indexes` is an increment list.
            while indexes and indexes[-1] > current:
                indexes.pop()
            indexes.append(current)

            if current + nums[current] >= terminal:
                return len(indexes)    # `current` can reach the last index!

            for index in range(current + 1, current + 1 + nums[current]):
                if index in went_index:
                    continue
                temp[index + nums[index]] = index
                went_index.add(index)

            # Let every current step be maximum.
            for _, index in sorted(temp.items()):
                steps.append(index)
            temp.clear()

        return len(indexes)


#%%    Main Function
Solution().jump([2, 3, 1, 1, 4])

#%%    Main
if __name__ == '__main__':
    pass

#%%
