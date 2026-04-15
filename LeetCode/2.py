#Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = anch = ListNode(-1)
        s = c = 0
        while l1 is not None and l2 is not None:
            t  = l1.val + l2.val + c
            s, c = t%10, t//10
            
            cur = ListNode(s)
            anch.next = cur
            anch = cur

            l1 = l1.next
            l2 = l2.next
        # !l1 or !l2, carry or !carry
        l = l1
        if l2 is not None:
            l = l2
        # l or !l, c or !c
        anch.next = l
        if not c:
            # l or !l , !c -> reuse l's tail in answer
            return ans.next
        # l or !l, c
        while l is not None and l.val == 9:
            l.val = 0
            anch = l
            l = l.next
        # l or !l, last carry
        if l is not None:
            # l, last carry
            l.val += 1
            return ans.next
        # !l, last carry (append 1)
        cur = ListNode(1)
        anch.next = cur
