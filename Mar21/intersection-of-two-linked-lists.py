# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getListSize(self, head):
        i = 0
        while head:
            head = head.next
            i += 1
        return i
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = self.getListSize(headA)
        b = self.getListSize(headB)
        
        if a > b:
            for _ in range(a-b):
                headA = headA.next
        elif b > a:
            for _ in range(b-a):
                headB = headB.next
        
        overlap = min(a, b)
        while overlap:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
            overlap -= 1
        
        return None