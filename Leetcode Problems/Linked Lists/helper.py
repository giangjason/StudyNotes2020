from listnode import ListNode
from typing import List

class Helper():

    @staticmethod
    def construct_linked_list(nums: List[int]) -> ListNode:
        """Constructs a singly linked linked list from the given array of number.

        Args:
            nums (List[int]): The array of numbers to construct the linked list.

        Returns:
            ListNode: The head node of the linked list.
        """
        head = tail = ListNode(nums[0]) if len(nums) > 0 else None
        for i in range(1, len(nums)):
            tail.next = ListNode(nums[i])
            tail = tail.next

        return head

    @staticmethod
    def convert_to_array(head: ListNode) -> List[int]:
        """Converts a linked list to an array.

        Args:
            head (ListNode): The head of the linked list.

        Returns:
            List[int]: An array containing the contents of the linked list.
        """
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        return nums