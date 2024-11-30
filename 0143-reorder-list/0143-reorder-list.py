# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # if not head:
        #     return head
        # current = head
        # stack =[]
        # counter= 0
        # #size
        # while current:
        #     counter+=1
        #     current =current.next
        # i= 0
        # current = head
        # while i <= counter//2 :

        #     current= current.next
        #     i+=1
        # while current:
        #     stack.append(current)
        #     corrent=current.next
        # corrent = head
        # while current:
        #     node = stack.pop()
        #     nextNode= current.next
        #     current.next= node
        #     node.next=nextNode
        #     current= current.next.next

        if not head or not head.next:
            return
        slow ,fast =head, head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        
        prev ,current = None ,slow.next
        slow.next= None
        
        #revers
        while current:
            temp =current.next
            current.next =prev
            prev = current
            current =temp

        first, second = head, prev

        while first and second:
            first2 ,second2= first.next, second.next
            first.next= second
            second.next= first2
            first ,second= first2 ,second2

        
