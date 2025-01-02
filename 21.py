
'''21. Merge Two Sorted Lists
Created on 2025-01-02 17:01:37
2025-01-02 17:24:40

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
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]
                      ) -> Optional[ListNode]:
        result: ListNode = ListNode()

        result_head = result    #record the head of `result`
        while list1 is not None and list2 is not None:
            number: int
            if list1.val < list2.val:    #get a smaller node
                number = list1.val
                list1 = list1.next
            else:
                number = list2.val
                list2 = list2.next

            result.next = ListNode(number)    #add the smaller node
            result = result.next

        # Add the rest of the nodes by linking to the remaining list.
        result.next = list1 if list2 is None else list2

        # Do not do it with travering!! Make good use of the pointer.
        #rest_list: Optional[ListNode] = list1 if list2 is None else list2
        #while rest_list is not None:    #add the rest of nodes
        #    result.next = ListNode(rest_list.val)
        #    result = result.next

        #    rest_list = rest_list.next

        return result_head.next


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
