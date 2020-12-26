# Write a program that accepts a linked list, L and an integer, K 
# and sorts the list so that all nodes less than K appear before K 
# and all nodes greater than K appear after K.
# Relative ordering of all values should remain the same after sorting.
# Ex. L = 2 3 11 7 5 6 10 7  |  K = 7
# Output = 2 3 5 6 7 7 11 10

# Two methods (both O(n))
# METHOD 1:
# Pivot the linked list from from to back, moving smaller elements to the front
# Reverse the linked list
# Pivot the linked list from back to front, moving larger elements to the back

# METHOD 2:
# Create three dummy nodes to keep track of less than, equal to, and greater than
# Traverse through the list and add the node to the appropriate node tracker (less, equal, greater)
# Combine less + equal + greater and return the combined list
# This is preferred since you won't have to reverse the list

from helper import Helper, ListNode
import random

def pivot_list(L: ListNode, K: int) -> ListNode:
    less_pre = less_tail = ListNode()
    equal_pre = equal_tail = ListNode()
    greater_pre = greater_tail = ListNode()
    curr = L
    while curr:
        if curr.val < K:
            less_tail.next = curr
            less_tail = less_tail.next
        elif curr.val == K:
            equal_tail.next = curr
            equal_tail = equal_tail.next
        else:
            greater_tail.next = curr
            greater_tail = greater_tail.next
        curr = curr.next

    greater_tail.next = None
    equal_tail.next = greater_pre.next
    less_tail.next = equal_pre.next
    return less_pre.next

def main():
    h = Helper()

    low, high = 0, 8
    length = 10

    nums = h.generate_random_list(low, high, length)
    k = nums[random.randint(0, length-1)]

    print("\n")
    print("Nums generated:", nums)
    print("K:", k)

    l = h.construct_linked_list(nums)
    pl = pivot_list(l, k)
    actual = h.convert_linked_list_to_array(pl)
    
    print("Actual:", actual)
    print("\n")
main()


