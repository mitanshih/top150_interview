
'''2. Add Two Numbers
Created on 2025-01-02 15:52:14
2025-01-02 16:46:38

@author: MilkTea_shih
'''

#%%    Packages
from typing import Optional

#%%    Variable
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#%%    Functions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # The description gives two non-empty linked lists, `l1` and `l2`,
    # so change the type hint from `Optional[ListNode]` to `ListNode`.
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        carry: int = 0

        result: ListNode = ListNode()
        result_head: ListNode = result    #record the head of `result`
        while l1 is not None or l2 is not None or carry == 1:
            number: int = ((l1.val if l1 is not None else 0)
                           + (l2.val if l2 is not None else 0)
                           + carry)

            # `curry`: 1 while `number` is bigger than 10; otherwise, 0.
            carry, number = divmod(number, 10)

            # Let both `l1` and `l2` reach the end and stop there.
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            result.next = ListNode(number)    #add the number of `node`
            result = result.next

        return result_head.next    #return the beginning number of `result`


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
