
'''61. Rotate List
Created on 2025-01-07 22:12:57
2025-01-07 22:39:56

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
    def rotateRight(self, head: Optional[ListNode], k: int
                    ) -> Optional[ListNode]:
        if head is None or k == 0:    #edge case and also `k` is 0, no rotate
            return head

        length: int = 1
        current: ListNode = head
        # Reach the node before the end of `head`.
        while current is not None and current.next is not None:
            length += 1

            current = current.next

        k %= length    # `k // length` is the times to rotate whole `head`.
        if k == 0:     # `k` equals zero, which indicates there is no rotated.
            return head

        # Let the end of node point to the beginning of `head`.
        current.next = head

        current = head
        # Reach the previous node at the rotated linked list.
        for _ in range(length - k - 1):
            current = current.next  # type: ignore

        head = current.next    # The beginning of the rotated linked list.
        current.next = None    # The end node of the rotated linked list.

        return head


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
