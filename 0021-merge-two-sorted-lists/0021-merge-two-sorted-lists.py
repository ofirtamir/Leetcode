# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1
        # if list1.val <= list2.val:
        #     res =list1
        #     curr1=list1.next
        #     curr2=list2
        # else:
        #     res = list2
        #     curr2= list2.next
        #     curr1=list1
        # current =res

        # while curr1 and curr2:
        #     if curr1.val <= curr2.val:
        #         current.next=curr1
        #         curr1=curr1.next
        #     else:
        #         current.next=curr2
        #         curr2=curr2.next
        #     current = current.next
            
        # if curr1:
        #     current.next=curr1
        # if curr2:
        #     current.next=curr2
        # return res
        dummy = ListNode()
        node =dummy
        while list1 and list2:
            if list1.val < list2.val:
                node.next=list1
                list1=list1.next
            else:
                node.next =list2
                list2= list2.next
            node= node.next
        # if list1:
        #     node.next= list1
        # elif list2:
        #     node.next =list2
        node.next =list1 or list2
        return dummy.next
