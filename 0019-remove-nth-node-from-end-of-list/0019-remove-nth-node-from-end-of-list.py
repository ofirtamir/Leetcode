# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if not head:
        #     return head
        # cur =head
        # size =0
        # while cur:
        #     size+=1
        #     cur=cur.next
        # cur =head
        # i =1
        # while i<size-n:
        #     cur= cur.next
        #     i+=1
        # if not cur.next:
        #     return head
        # cur.next=cur.next.next
        # return head
        if not head.next and n==1:
            head =None
            return head
        if not head:
            return head
        prav, cur =None, head
        size=0
        while cur:
            size+=1
            cur=cur.next
        cur= head
        rem= size-n
        i=0
        while i<rem:
            prav =cur
            cur= cur.next
            i+=1
        if rem == 0:
            head= head.next
            return head
        prav.next= cur.next
        return head

        