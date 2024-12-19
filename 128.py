
'''128. Longest Consecutive Sequence
Created on 2024-12-19 15:45:40

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        table: dict[int, int] = {}  #number: consecutive_length
        result: int = 0
        for number in nums:
            if number in table:    #avoid duplicate
                continue

            #get the length from `previous` and `next` number
            previous_number_length: int = table.get(number - 1, 0)
            next_number_length: int = table.get(number + 1, 0)

            length: int = previous_number_length + next_number_length + 1
            table[number] = length    #lengh of current number

            #update the consecutive length at *lower* and *upper* bound
            table[number - previous_number_length] = length
            table[number + next_number_length] = length

            result = max(result, length)

        return result


class Solution_reference:
    # `n - 1` does not exist at the beginning of the consecutive length,
    # and iterates to the end of the consecutive length.
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set: set[int] = set(nums)
        result: int = 0

        for n in nums:
            if n - 1 not in num_set:  #the beginning of consecutive length
                length: int = 1

                while n + length in num_set:  #find the end
                    length += 1

                result = max(result, length)

        return result


#%%    Main Function
Solution().longestConsecutive([-1, 100, 4, 200, 1, 3, 2, 0, 2])

#%%    Main
if __name__ == '__main__':
    pass

#%%
