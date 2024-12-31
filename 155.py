
'''155. Min Stack
Created on 2024-12-31 12:41:51
2024-12-31 13:10:38

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
"""    Constraints:
Methods except `push()` operations is always called on non-empty stacks
"""
#https://leetcode.com/problems/min-stack/solutions/3775651/python-99-95-faster-only-one-stack/
class MinStack_single_store:
    """    core thought: encode the minimum while pushing into `stack`
    self.min < old_min
    2 * self.min < old_min + self.min
    2 * self.min - old_min < self.min
    2 * val - old_min < self.min
    """

    def __init__(self) -> None:
        self.stack: list[int] = []  #stack
        self.min: int = None  # type: ignore  #min element

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min = val
        elif val >= self.min:    #same logic in `top()`: self.stack[-1] >= min
            self.stack.append(val)
        else:                    #same logic in `pop()`: self.stack[-1] < min
            self.stack.append(2 * val - self.min)
            self.min = val

    def pop(self) -> None:
        last: int = self.stack.pop()
        if last < self.min:
            self.min = 2 * self.min - last

    def top(self) -> int:
        return self.stack[-1] if self.stack[-1] >= self.min else self.min

    def getMin(self) -> int:
        return self.min


class MinStack:
    def __init__(self) -> None:
        self.stack: list[list[int]] = []  #[value, current_min_value]

    def push(self, val: int) -> None:
        self.stack.append(
            [val,
             #get the last minimum and compare to `val` for lastest minimum
             min(val, self.getMin()) if self.stack else val]
        )

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(val)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()


#%%    Main Function
a = MinStack_single_store()

#%%    Main
if __name__ == '__main__':
    pass

#%%
