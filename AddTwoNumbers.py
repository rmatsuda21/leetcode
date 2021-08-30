# https://leetcode.com/problems/add-two-numbers/solution/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 1 if (l1.val + l2.val) >= 10 else 0
        root = ListNode((l1.val + l2.val) % 10, None)
        currNode = root
        l1 = l1.next
        l2 = l2.next
        
        while l1 or l2 or carry:
            curVal = 0
            if l1 and l2:
                curVal = l1.val + l2.val + carry
            elif l1:
                curVal = l1.val + carry
            elif l2:
                curVal = l2.val + carry
            else:
                curVal = carry
            
            if curVal >= 10:
                curVal = curVal % 10
                carry = 1
            else:
                carry = 0
            
            node = ListNode(curVal, None)
            currNode.next = node
            currNode = node
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return root