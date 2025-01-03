
'''92. Reverse Linked List II
Created on 2025-01-03 17:07:48

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
    def reverseBetween(self, head: Optional[ListNode],
                       left: int,
                       right: int
                       ) -> Optional[ListNode]:
        if left == right:
            return head

        dummy: ListNode = ListNode(next=head)

        previous: ListNode = dummy
        for _ in range(left - 1):
            previous = previous.next

        current: ListNode = previous.next
        for _ in range(right - left):
            temp: ListNode = current.next

            current.next = temp.next
            temp.next = previous.next  #backward
            previous.next = temp

        return dummy.next


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
