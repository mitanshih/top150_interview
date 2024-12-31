
'''150. Evaluate Reverse Polish Notation
Created on 2024-12-31 14:16:38
2024-12-31 14:46:34

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []
        for token in tokens:
            match token:
                case '+':
                    stack[-1] = stack.pop() + stack[-1]
                case '-':
                    stack[-1] = stack[-2] - stack.pop()
                case '*':
                    stack[-1] = stack.pop() * stack[-1]
                case '/':
                    stack[-1] = int(stack[-2] / stack.pop())
                case _:
                    stack.append(int(token))

            #
        return stack[0]


#%%    Main Function
Solution().evalRPN(
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
)

#%%    Main
if __name__ == '__main__':
    pass

#%%
