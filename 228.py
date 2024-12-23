
'''228. Summary Ranges
Created on 2024-12-20 15:51:32
2024-12-20 16:35:35

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if nums == []:
            return []

        result: list[str] = []
        start: int = nums[0]
        nums.append(nums[-1])  #add 1 more check for the final element

        for index, number in enumerate(nums[1:]):
            #check `nums[index - 1]` with `nums[index]` which is `number`
            if nums[index] + 1 != number:    #find inconsecutive number
                result.append(
                    str(start) if start == nums[index]    #inconsecutive case
                    else f"{start}->{nums[index]}"    #consecutive number
                )

                start = number    #update the beginning of the interval

        return result


class Solution_:
    def add_consecutive_number(self, result: list[str], interval: list[int]
                               ) -> list[str]:
        match len(interval):
            case 1:  #not consecutive number
                result.append(str(interval[0]))
            case 2:  #consecutive number
                #result.append("->".join(map(str, interval)))
                result.append(f"{interval[0]}->{interval[1]}")

        return result

    def summaryRanges(self, nums: list[int]) -> list[str]:
        if nums == []:
            return []

        result: list[str] = []
        interval: list[int] = [nums[0]]  #[left_number, right_number]

        for number in nums[1:]:
            if number - 1 == interval[0]:
                interval.append(number)  #right_number
            elif len(interval) == 2 and number - 1 == interval[1]:
                interval[1] = number    #update right_number
            else:    #find inconsecutive number
                result = self.add_consecutive_number(result, interval)

                interval.clear()    #initialize
                interval.append(number)  #add current left_number

        return self.add_consecutive_number(result, interval)  #final case


#%%    Main Function
Solution().summaryRanges([0, 1, 2, 4, 5, 7])

#%%    Main
if __name__ == '__main__':
    pass

#%%
