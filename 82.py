
'''82. Remove Duplicates from Sorted List II
Created on 2025-01-06 15:36:34
2025-01-06 17:04:44

@author: MilkTea_shih
'''

#%%    Packages
from typing import Optional, Self

#%%    Variable
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: Optional[Self] = next

#%%    Functions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]
                         ) -> Optional[ListNode]:
        dummy_head: ListNode = ListNode(next=head)  #add 1 node for edge case
        not_duplicate: ListNode = dummy_head

        # `head` precedes `not_duplicate` by 1 node.
        while head is not None:
            if head.next is not None and head.val == head.next.val:
                while head.next is not None and head.val == head.next.val:
                    head = head.next    #skip duplicate nodes

                not_duplicate.next = head.next    #connect passing node
            else:    #add not duplicate node
                not_duplicate = not_duplicate.next  # type: ignore

            head = head.next

        return dummy_head.next


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
