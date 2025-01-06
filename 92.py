
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

        # Add 1 more node while the left is 1 is changing the first of `head`.
        dummy_head: ListNode = ListNode(next=head)

        previous: ListNode = dummy_head
        #find the binginning place to reserve
        for _ in range(left - 1):
            previous = previous.next  #1 -> 2 -> 3 -> 4 -> 5 -> 6 -> N

        #reverse the nodes in the range
        #practice [left, right] is [2, 5] and head is `1 -> 2 -> … -> 6 -> N`
        current: ListNode = previous.next  #2 -> 3 -> 4 -> 5 -> 6 -> N
        for _ in range(right - left):
            #iterate
            temp: ListNode = current.next  #3 -> 4 -> 5 -> 6 -> N
            #4 -> 5 -> 6 -> N
            #5 -> 6 -> N

            #split
            current.next = temp.next  #*2* -> 4 -> 5 -> 6 -> N
            #*2* -> 5 -> 6 -> N
            #*2* -> 6 -> N

            #backward
            temp.next = previous.next  #*3* -> 2 -> 4 -> 5 -> 6 -> N
            #*4* -> 3 -> 2 -> 5 -> 6 -> N
            #*5* -> 4 -> 3 -> 2 -> 6 -> N

            #connect
            previous.next = temp  #*1* -> 3 -> 2 -> 4 -> 5 -> 6 -> N
            #*1* -> 4 -> 3 -> 2 -> 5 -> 6 -> N
            #*1* -> 5 -> 4 -> 3 -> 2 -> 6 -> N

        return dummy_head.next


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
