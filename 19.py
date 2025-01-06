
'''19. Remove Nth Node From End of List
Created on 2025-01-06 14:29:35
2025-01-06 15:08:04

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int
                         ) -> Optional[ListNode]:
        #len(head) = x
        # The last n-th node index is *x - n*.
        #remove distance to the end is *x - n - 1* node
        dummy_head: ListNode = ListNode(next=head)  #add 1 node for edge case

        current: ListNode = dummy_head
        head = dummy_head
        for _ in range(n + 1):    #move forward `n + 1` indexes
            head = head.next  # type: ignore

        # `head` is `n + 1` indexes from `head`.
        # `current` contains *x - n - 1* indexes guided by `head` to the end.
        while head is not None:
            head = head.next
            current = current.next

        assert isinstance(current.next, ListNode)
        current.next = current.next.next    #remove last `n`-th node

        return dummy_head.next


#%%    Main Function

#%%    Main
if __name__ == '__main__':
    pass

#%%
