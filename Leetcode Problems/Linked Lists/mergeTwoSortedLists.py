from listnode import ListNode

class Solution():

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = tail = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tail.next = ListNode(l2.val)
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        return prehead.next
