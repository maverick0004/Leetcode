# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        def f(node, pos, length):
            
            if not node:
                f.k = length - f.k
                return
            
            if pos == f.k:
                f.first = node
            
            f(node.next, pos+1, length + 1)
            
            if pos == f.k:
                f.second = node
        
        f.k = k
        f.first = None
        f.second = None
        f(head, 1, 1)
        if f.first != f.second:
            f.first.val, f.second.val = f.second.val, f.first.val
        
        return head
