# Write a program that takes a singly linked list, and two integers s and f as args 
# and reverses the reverses the nodes from sth to fth inclusive. 
# The numbering begins at 1, i.e, the head node is the first node. 
# Do not allocate extra nodes.
# Ex. input = 11 -> 3 -> 5 -> 7 -> 2 | s = 2 f = 4
#     output = 11 -> 7 -> 5 -> 3 -> 2

# Pseudo code:
# Find the node that correlates to the node before s
# Find the node that correlates to the node after f
# Find the sublist s - f
# Reverse the sublist s-f
# Merge the sublist back into the original list

from helper import Helper, ListNode
from typing import List, Tuple


def reverse_single_sublist(head: ListNode, s: int, f: int) -> ListNode:
    count = 1
    # Find nodes associated pre-s and post-f
    curr = head
    pre_s_node, post_f_node = None, None
    s_node, f_node = None, None
    while f_node is None:
        # Find pre-s and s-node
        if count == s - 1:
            pre_s_node = curr
        elif count == s:
            s_node = curr
        # Find post-f and f-node
        elif count == f:
            f_node = curr
            post_f_node = curr.next

        curr = curr.next
        count += 1

    # Reverse the sublist
    # f_node is now the head of the sublist
    reverse_single_sublist_helper(s_node, f_node)

    # Merge the sublist back into the list
    if pre_s_node:
        pre_s_node.next = f_node
    else:
        head = f_node
    s_node.next = post_f_node

    return head


def reverse_single_sublist_helper(s_node: ListNode, f_node: ListNode) -> None:
    pre = None
    curr = s_node
    while curr and pre is not f_node:
        tmp = curr.next
        curr.next = pre
        pre = curr
        curr = tmp

        


def main():
    print("\n")

    h = Helper()

    low = 1
    high = 100
    length = 7
    nums = h.generate_random_list(low, high, length)

    print("Nums:",nums)

    s = 1
    f = 5

    rev = nums[s-1:f]
    rev.reverse()
    expected = nums[:s-1] + rev + nums[f:]

    print("S: {0}. Nums[S]: {1}".format(s, nums[s-1]))
    print("F: {0}. Nums[F]: {1}".format(f, nums[f-1]))
    print("Expected:", expected)

    ll = h.construct_linked_list(nums)
    actual = reverse_single_sublist(ll, s, f)
    actual_arr = h.convert_linked_list_to_array(actual)

    print("Actual:\t", actual_arr)

    print("\n")
main()
