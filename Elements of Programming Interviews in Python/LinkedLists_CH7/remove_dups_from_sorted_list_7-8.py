# Write a program that takes in a sorted linked list of integers and removes all duplicates
# Ex. 1 2 3 4 4 4 4 5 6 7 7 8 9 10
# output = 1 2 3 4 5 6 7 8 9 10

from helper import Helper, ListNode

def remove_duplicates(head: ListNode) -> None:
    first, second = head, head.next
    while second:
        if first.val != second.val:
            first.next = second
            first = second
        second = second.next
    first.next = second
    

def main():
    h = Helper()
    low = 0
    high = 7
    length = 20

    nums = sorted(h.generate_random_list(low, high, length))

    ll = h.construct_linked_list(nums)
    remove_duplicates(ll)
    
    expected = set(nums)
    actual = h.convert_linked_list_to_array(ll)

    print("\n")
    print("Nums generated:", nums)
    print("Expected:", expected)
    print("Actual:", actual)
    print("\n")
main()
