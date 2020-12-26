# Write a program that takes two linked lists representing two different integers, 
# with the least significant digit appearing first, and add them together.
# Ex. l1 = 1 2 3 | l2 =  4 5 6
# output = 5 7 9

from helper import Helper, ListNode
import sys

def add_lists(l1: ListNode, l2: ListNode) -> ListNode:
    prehead = tail = ListNode()
    carry = 0
    while l1 or l2 or carry: 
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        l_sum = l1_val + l2_val + carry
        carry = l_sum // 10
        tail.next = ListNode(l_sum % 10)
        tail = tail.next 

    return prehead.next

def main():
    h = Helper()

    low, high = 0, 9
    length1 = 4
    length2 = 3

    args = sys.argv
    if len(args) > 1:
        l1_nums = [int(arg) for arg in list(args[1])]
        l2_nums = [int(arg) for arg in list(args[2])]
    else:
        l1_nums = h.generate_random_list(low, high, length1)
        l2_nums = h.generate_random_list(low, high, length2)

    print("\n")
    print("L1:", l1_nums)
    print("L2:", l2_nums)

    l1 = h.construct_linked_list(l1_nums)
    l2 = h.construct_linked_list(l2_nums)

    l_sum = add_lists(l1, l2)
    l_sum_arr = h.convert_linked_list_to_array(l_sum)

    print("L1+L2:", l_sum_arr)
    print("\n")

main()