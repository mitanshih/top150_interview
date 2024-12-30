
'''20. Valid Parentheses
Created on 2024-12-30 14:54:41
2024-12-30 15:34:48

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False    # There is at least 1 bracket that is not closed.

        left_brackets: list[str] = []
        bracket_paired_table: dict[str, str] = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for bracket in s:
            if bracket not in bracket_paired_table:    #append left bracket
                left_brackets.append(bracket)
            elif (not left_brackets    # `bracket` is the right bracket.
                  or left_brackets.pop() != bracket_paired_table[bracket]):
                return False    # `bracket` is paired with the wrong bracket.

        return not left_brackets  # True: len(left_brackets) == 0, else False.


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False    # There is at least 1 bracket that is not closed.

        left_brackets: list[str] = []
        for bracket in s:
            match bracket:
                case '(' | '[' | '{':    #append left bracket
                    left_brackets.append(bracket)
                case _:    # The right bracket is paired with the left bracket.
                    if left_brackets:
                        match left_brackets.pop():    #paired in ordered
                            case '(':
                                if bracket != ')':
                                    break
                            case '[':
                                if bracket != ']':
                                    break
                            case '{':
                                if bracket != '}':
                                    break
                        #
                    else:    # There is no left bracket paired with right's.
                        break
            #
        else:
            return False if left_brackets else True    #check `left_brackets`
        return False


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
