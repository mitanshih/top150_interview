
'''202. Happy Number
Created on 2024-12-18 16:58:37
2024-12-18 17:32:21

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    # Reference for another thought by using fast-slow pointer to do.
    # If fast pointer can not find 1, it catches up with slow pointer.
    def isHappy(self, n: int) -> bool:
        seen_number: set[int] = set()

        while n not in seen_number:
            seen_number.add(n)

            number: int = 0
            while n >= 10:
                n, remainder = divmod(n, 10)    #take last digit of `n`
                number += remainder ** 2

            number += n ** 2    #the first and rest digit of `n`
            if number == 1:
                return True

            n = number

        return False


#%%    Main Function
Solution().isHappy(7)

#%%    Main
if __name__ == '__main__':
    pass

#%%
