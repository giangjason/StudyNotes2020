# Write an algorithm that takes an array of intergers, arr, and returns the top k, values of the array.
# Ex. arr = [2,8,1,7,6,10,8,9], k = 3. Output = [8,9,10]

from typing import List
import random
import heapq

def find_top_k_elements(nums: List[int], k: int) -> List[int]:
    count = 0
    min_heap = []
    for num in nums:
        if count >= k:
            heapq.heappushpop(min_heap, num)
        else:
            heapq.heappush(min_heap, num)
        count += 1

    return min_heap

def main():
    nums = [6,10,8,9,2,1]
    k = 1
    result = find_top_k_elements(nums, k)
    print(result)
main()