# Write a program that takes a linked list and an integer, K, 
# and returns the list cyclically shifted to the right K times.
# Ex. L = 2 3 5 3 2, K = 3
# output = L = 5 3 2 2 3

# Pseudo code
# Define two pointers, one starting at the head, one starting K-1 nodes away.
# This will be our K-lengthed window
# Define a pointer that will track the pointer previously visited by the first pointer, (pre)
# Iterate the first and second pointers in tandem by one, when the second pointer reaches the end, 
# the first will be pointing to the beginning of the window.
# Move the node window to the beginning of the list
# Remove the next pointer of the (pre) tracking pointer

from helper import Helper, ListNode
import random
import sys

def right_shift_list(head: ListNode, k: int) -> ListNode:
    pre = ListNode(0, head)
    first = second = head
    for _ in range(k-1):
        second = second.next

    while second.next:
        pre = pre.next
        first = first.next
        second = second.next

    pre.next = None
    second.next = head
    return first

def main():
    h = Helper()

    low, high = 0, 20
    length = 5

    args = sys.argv
    if len(args) > 1:
        k = int(args[1])
        nums = [int(arg) for arg in list(args[2:])]
    else:
        k = random.randint(1, length-1)
        nums = h.generate_random_list(low, high, length)

    k = length

    print("\n")
    print("Nums:", nums)
    print("K:", k)

    l = h.construct_linked_list(nums)
    rl = right_shift_list(l, k)

    expected = nums[len(nums)-k:] + nums[:len(nums)-k]
    actual = h.convert_linked_list_to_array(rl)

    print("Expected:", expected)
    print("Actual:", actual)
    print("\n")

main()

