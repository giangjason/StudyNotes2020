from listnode import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        curr = head
        while curr:
            new_head = ListNode(curr.val, new_head)
            curr = curr.next
        return new_head