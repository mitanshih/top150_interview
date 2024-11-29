
'''125. Valid Palindrome
Created on 2024-11-29 22:20:33

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    #Time: O(2n)
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s.lower()))
        return s == s[::-1]


class Solution:
    #Time: O(n + n/2)
    def isPalindrome(self, s: str) -> bool:
        str_list: list[str] = [string.lower() for string in s
                               if string.isalnum()]

        middle: int = len(str_list) // 2
        return str_list[:middle] == str_list[len(str_list):-middle - 1:-1]


class Solution_two_pointer:
    #Time: O(n)
    def isPalindrome(self, s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1

        while left < right:
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            # skip not *alphanumeric* string
            elif not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            #
            else:    #s[left].lower() != s[right].lower()
                return False
        return True


#%%    Main Function
Solution().isPalindrome("A man, a plan, a canal: Panama")

#%%    Main
if __name__ == '__main__':
    pass

#%%
