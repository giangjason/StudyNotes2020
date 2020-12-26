# Write a program that checks if a linked list is palindromic

# Pseudo code:
# Find the length of the list
# Find the middle node of the list which is length // 2 + 1
# Reverse the second half of the list
# Create two pointers, one at the front, one at the end
# Iterate in tandem towards the middle, if the values differ at any point, return false
# If left and right pass each other, it means the list is palindromic, return true at the end.

from helper import Helper, ListNode
import sys

def get_length(head: ListNode) -> int:
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    return length

def reverse_list(node: ListNode) -> ListNode:
    ''' Returns the tail of the list'''
    prev = node
    curr = node.next
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev

def check_palindromic(head: ListNode) -> bool:
    length = get_length(head)
    mid = length // 2 + 1
    count = 1
    mid_node = head
    while count < mid:
        mid_node = mid_node.next
        count += 1

    first, first_counter= head, 1
    second, second_counter = reverse_list(mid_node), length

    while first_counter < second_counter: 
        if first.val != second.val:
            return False
        
        first = first.next
        first_counter += 1

        second = second.next
        second_counter -= 1

    return True


def main():
    h = Helper()

    args = sys.argv
    if len(args) > 1:
        values = args[1:]
    else:
        values = [1,2,3,4,5]

    l = h.construct_linked_list(values)
    is_palindromic = check_palindromic(l)

    print("\n")
    print("Values:", values)
    print("Is palindromic:", is_palindromic)
    print("\n")

main()
    

