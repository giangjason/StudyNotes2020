# Write a program that takes an array A and an index i into A, and rearranges the elements such that 
# all elements less than A[i] (the "pivot") appear first, 
# followed by elements equal to the pivot, 
# followed by elements greater than the pivot.

# Pseudo code: 
# Think of how partitioning works in quick sort
# Iterate through the list once, move items less than the pivot to the left
# Iterate through the list again, this time from the back to front, moving items greater than the pivot to the back

from typing import List
import random
import sys

def parition_array(A: List[int], i: int) -> None:
    p = A[i]
    j = -1
    for i in range(len(A)):
        if A[i] < p:
            j += 1
            A[i], A[j] = A[j], A[i]

    k = len(A)
    for h in range(len(A)-1, -1, -1):
        if A[h] > p:
            k -= 1
            A[h], A[k] = A[k], A[h]

def generate_random_nums(low: int, high: int, length: int) -> List[int]:
    return [random.randint(low, high) for _ in range(length)]            

def main():

    low = 0
    high = 8
    length = 15

    args = sys.argv
    if len(args) > 1:
        low = int(args[1])
        high = int(args[2])
        length = int(args[3])
        
    i = random.randint(low, length)
    nums = generate_random_nums(low, high, length)
    print("Pivot:", nums[i])
    print("Before:", nums)
    parition_array(nums, i)
    print("After:", nums)
main()



