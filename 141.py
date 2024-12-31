
'''141. Linked List Cycle
Created on 2025-01-01 01:13:43
2025-01-01 01:34:34

@author: MilkTea_shih
'''

#%%    Packages
from typing import Optional

#%%    Variable
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#%%    Functions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution_reference:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head is not None:
            if head.val is None:
                return True

            head.val = None
            head = head.next

        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while slow and fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
