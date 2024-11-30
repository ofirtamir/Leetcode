# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        cur= l1
        while cur:
            s1 = str(cur.val)+s1
            cur=cur.next
        cur= l2
        while cur:
            s2 = str(cur.val)+s2
            cur= cur.next

        s12 = int(s1)+int(s2)
        if s12 == 0:
            return ListNode(0)
        li = []
        while s12 >0:
            li.append(ListNode(s12 % 10))
            s12=s12//10
        for i in range(len(li)-1):
            li[i].next = li[i+1]
        return li[0]

