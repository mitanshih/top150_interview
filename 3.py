
'''3. Longest Substring Without Repeating Characters
Created on 2024-12-09 14:33:00
2024-12-09 15:18:08

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_single_loop:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen_table: dict[str, int] = {}    #key: string, value: index
        last_index: int = -1  # The length from begin to index is `index + 1`.

        result: int = 0

        for index, string in enumerate(s):
            last_index = max(last_seen_table.get(string, -1), last_index)
            result = max(index - last_index, result)

            last_seen_table[string] = index

        return result


class Solution_reference:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_start: int = 0
        string_table: dict[str, int] = {}    #key: string, value: count

        result: int = 0

        for index, string in enumerate(s):
            string_table[string] = string_table.get(string, 0) + 1
            while string_table[string] > 1:
                string_table[s[substring_start]] -= 1
                substring_start += 1

            result = max(index - substring_start + 1, result)

        return result


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_start: int = 0
        substring: set[str] = set()

        result: int = 0

        for string in s:
            if string in substring:
                result = max(len(substring), result)
                #remove all elements before `string` in `substring`
                while s[substring_start] != string:
                    substring.remove(s[substring_start])
                    substring_start += 1
                substring_start += 1
            else:
                substring.add(string)

        return max(len(substring), result)


#%%    Main Function
Solution().lengthOfLongestSubstring("abcabcbb")

#%%    Main
if __name__ == '__main__':
    pass

#%%
