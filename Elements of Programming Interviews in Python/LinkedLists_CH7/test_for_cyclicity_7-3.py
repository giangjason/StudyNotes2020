# Write a program that takes the head of a singly linked list 
# and returns the beginning node of the cycle if a cycle exists, other wise, null.

# Define a slow and fast pointer
# Iterate through the linked list, 
# if the slow pointer gets to the end of the linked list without the ever meeting the fast pointer,
# the list does not have a cycle.
# If the slow pointer and fast pointer ever meet, there is a cycle.

# To find the length of the cycle, start with a node within the cycle, 
# count the number of nodes encountered until the node started with is encountered again      

# To find the start of the cycle, let C = length of the cycle
# Have two pointers, one at the head, and one that is C away from the first pointer.
# Traverse until the two pointers meet, the node where the meet is the start of the cycle

from helper import Helper, ListNode
from typing import List
import random

def get_node_in_cycle(head: ListNode) -> ListNode:
    slow, fast = head, head.next
    while fast.next.next:
        if slow == fast:
            return slow
        fast = fast.next.next
        slow = slow.next
    return None

def get_cycle_length(node: ListNode) -> int:
    count = 1
    curr = node.next
    while curr:
        if curr is node:
            return count
        curr = curr.next
        count += 1

def get_start_of_cycle(head: ListNode) -> ListNode:
    node_in_cycle = get_node_in_cycle(head)
    if node_in_cycle is None:
        return None
    
    cycle_length = get_cycle_length(node_in_cycle)

    # Define the first and second
    first = second = head

    # Position the second pointer c_length away from the first pointer
    for _ in range(cycle_length):
        second = second.next

    while first:
        if first is second:
            return first
        first = first.next
        second = second.next

# def main():                              

#     h = Helper()
#     low = 1
#     high = 100
#     length = 5
#     nums = h.generate_random_list(low, high, length)

#     c = random.randint(0, length-1)
#     c = 4
#     cl = h.construct_cyclicle_linked_list(nums, c)

#     print("\n")
#     print("Nums generated:", nums)
#     print("Cycle starts:", nums[c])
#     print("Expected:", nums[c])

#     cycle_node = get_start_of_cycle(cl)
#     print("Actual: {0}".format(cycle_node.val if cycle_node else None))

#     print("\n")
# main()

def main():                              

    h = Helper()
    low = 1
    high = 100
    length = 5
    nums = h.generate_random_list(low, high, length)

    c = random.randint(0, length-1)
    c = 4
    cl = h.construct_linked_list(nums)

    print("\n")
    print("Nums generated:", nums)
    print("Cycle starts:", None)
    print("Expected:", None)

    cycle_node = get_start_of_cycle(cl)
    print("Actual: {0}".format(cycle_node.val if cycle_node else None))

    print("\n")
main()
