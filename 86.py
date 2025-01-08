
'''86. Partition List
Created on 2025-01-08 13:44:49
2025-01-08 14:57:53

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
    def partition(self, head: Optional[ListNode], x: int
                  ) -> Optional[ListNode]:
        dummy_node: ListNode = ListNode()    #edge case for partition at first
        partition: ListNode = ListNode()     #store with *another* linked list

        current: ListNode = dummy_node
        partition_head: ListNode = partition
        while head is not None:
            # Sperate node by its value is smaller or not smaller than `x`.
            if head.val < x:
                current.next = head
                current = current.next
            else:
                partition.next = head
                partition = partition.next

            head = head.next

        partition.next = None    #the end of the new linked list
        current.next = partition_head.next    #connect smaller and `partition`

        return dummy_node.next


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
