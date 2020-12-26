# Write a program that takes a linked list and sorts the list 
# so that all even numbers are on the left and all odd numbers are on the right.

# Pseudo code:
# Make two pointers, one to iterate through the list 
# and one to keep track of the even sublist (initalize it to before the beginning of the list)
# When the iterating pointer encounters an even number, 
# increment the even-tracking pointer by one and swap the values at the two pointers.
# When the iterating pointer reaches the end of the list, the list will have been sorted.

from helper import Helper, ListNode
from typing import List

def even_odd_merge(head: ListNode) -> None:
    first = ListNode(0, head)
    second = head
    while second:
        if second.val % 2 == 0:
            first = first.next
            first.val, second.val = second.val, first.val
        second = second.next
    

def get_actual(nums: List[int]) -> List[int]:
    evens, odds = [], []
    for num in nums: 
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens + odds

def main():
    h = Helper()

    low, high = 0, 10
    length = 3
    nums = h.generate_random_list(low, high, length)

    l = h.construct_linked_list(nums)
    even_odd_merge(l)
    l_arr = h.convert_linked_list_to_array(l)

    expected = get_actual(nums)
    actual = l_arr

    print("\n")
    print("Nums generated:", nums)
    print("Expected:", expected)
    print("Actual:", actual)

    print("\n")
main()
    
