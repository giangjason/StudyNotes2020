from __future__ import annotations
from typing import List
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Helper():

    def generate_random_list(self, low: int, high: int, length: int) -> List[int]:
        return [random.randint(low, high) for _ in range(length)]

    def construct_linked_list(self, nums: List[int]) -> ListNode:
        if len(nums) == 0:
            return None

        head = tail = ListNode(nums[0])
        for i in range(1, len(nums)):
            tail.next = ListNode(nums[i])
            tail = tail.next
        return head

    def convert_linked_list_to_array(self, root: ListNode) -> List[int]:
        nums = []
        curr = root
        while curr:
            nums.append(curr.val)
            curr = curr.next
        return nums

    def construct_cyclicle_linked_list(self, nums: List[int], c: int) -> ListNode:
        if len(nums) == 0:
            return None

        prehead = tail = ListNode()
        cycle = None
        for i in range(len(nums)):
            tail.next = ListNode(nums[i])
            if i == c:
                cycle = tail.next
            tail = tail.next
        tail.next = cycle
        return prehead.next