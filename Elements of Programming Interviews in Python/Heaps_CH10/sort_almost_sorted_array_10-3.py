# Write a program that takes an input a k-sorted array of integers and returns a completely sorted list of integers.
# A k-sorted array is defined as each number is at most k away from its correctly sorted position. 
# Ex. arr = [3, -1, 2, 6, 4, 5, 8], k = 2. Each item in arr is no more than k=2 away from its final sorted position
# Brownie points if you can do in place


from typing import List
import heapq

def sort_k_sorted_array(arr: List[int], k: int) -> None:
    heap = []
    replace_idx = 0
    for i in range(len(arr)):
        if len(heap) < k:
            heapq.heappush(heap, arr[i])
        else:
            num = heapq.heappushpop(heap, arr[i])
            arr[replace_idx] = num
            replace_idx += 1

    while replace_idx < len(arr):
        num = heapq.heappop(heap)
        arr[replace_idx] = num
        replace_idx += 1

def main():
    nums = [3, -1, 2]
    k = 2
    sort_k_sorted_array(nums, k)
    print(nums)
main()
