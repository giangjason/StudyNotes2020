# Write a program that takes a list head, head, and integer, k, 
# and removes the kth last element from the list. That is kth node from the end.
# Ex. head = 1 2 3 4 5 6 7 8 9 10, k = 3
# output = 1 2 3 4 5 6 7 9 10. 8 is the 3rd last element.

# Pseudo code
# We can find the kth last element by creating a window sized k nodes 
# Create window by creating two pointers, 1 at the beginning, 1 at k-1 nodes away
# Iterate the two pointers in tandem until the further pointer reaches the end, 
# the first pointer should be at the kth last node.

from helper import Helper, ListNode
from typing import List
import random

def remove_kth_element(head: ListNode, k: int) -> None:
    if k == 0:
        return

    # Define the first and second pointers
    first = second = head

    # Position the second k-1 nodes away
    for _ in range(k-1):
        second = second.next
    
    # Iterate in tandem, keeping track of the prev node visited in case of deleting last node in list
    prev = None
    while second.next:
        prev = first
        first = first.next
        second = second.next

    # If the kth node is not a last node, delete the node
    if first.next:
        delete_node(first)
    else:
        # If kth node is the last node, set the prev node's next to null
        prev.next = None
    
def delete_node(node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next

def main():
    h = Helper()

    low = 0
    high = 100
    length = 10

    nums = h.generate_random_list(low, high, length)
    head = h.construct_linked_list(nums)
    k = random.randint(0, length-1)
    k = 1
    remove_kth_element(head, k)
    head_arr = h.convert_linked_list_to_array(head)

    print("\n")
    print("Nums generated:", nums)
    print("K value:", k)
    print("Node to remove:", nums[length-k])

    del nums[length-k]
    expected = nums
    actual = head_arr

    print("Expected:", expected)
    print("Actual:", actual)

    print("\n")
main()
    
