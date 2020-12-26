# Write a program that takes in a linked list head and a node
# Delete the given node from the linked list
# Ex. 1 2 3 4 5 6, n = 4
# output = 1 2 3 5 6

from helper import Helper, ListNode
from typing import List
import random


def delete_node_from_list(node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next

def get_delete_node(head: ListNode, delete_idx: int) -> ListNode:
    idx = 0
    curr = head
    while curr:
        if idx == delete_idx:
            return curr
        idx += 1
        curr = curr.next
    return None

def main():
    h = Helper()
    low = 0
    high = 100
    length = 4

    nums = h.generate_random_list(low, high, length)

    l = h.construct_linked_list(nums)
    delete_idx = random.randint(0, length-2)

    print("\n")
    print("Nums generated:", nums)
    print("Num to delete:", nums[delete_idx])

    delete_node = get_delete_node(l, delete_idx)
    delete_node_from_list(delete_node)

    del nums[delete_idx]
    expected = nums
    actual = h.convert_linked_list_to_array(l)
    
    print("Expected:", expected)
    print("Actual:", actual)

    print("\n")
main()