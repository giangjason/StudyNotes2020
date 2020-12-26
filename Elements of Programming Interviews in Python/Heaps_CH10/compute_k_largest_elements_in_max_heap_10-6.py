# Design an algo to compute the top k elements in a max heap without modifying the heap

# Pseudo code:
# 1) Create a max heap
# 2) create an output array
# 3) Add the first item in the heap into out max heap
# 4) until the output array contains k elements, add the pop and add the top item of heap into the ouput array,
#   add any left children, add any right children
# 5) return the output array


from typing import List
from queue import Queue
import random
import heapq

def generate_random_list(length: int) -> List[int]:
    return [random.randint(0, 400) for _ in range(length)]

def compute_top_k_elements(heap: List[int], k: int) -> List[int]:
    max_heap, output = [], []
    
    curr_idx = 0
    heapq.heappush(max_heap, (-heap[curr_idx], curr_idx))
    while len(output) < k:
        # Get top value and index
        top = heapq.heappop(max_heap)
        curr_val = -top[0]
        curr_idx = top[1]

        # Add the top value to the output
        output.append(curr_val)

        # Add any left children
        left_idx = 2 * curr_idx + 1
        if left_idx < len(heap):
            heapq.heappush(max_heap, (-heap[left_idx], left_idx))

        # Add any right children
        right_idx = 2 * curr_idx + 2
        if right_idx < len(heap):
            heapq.heappush(max_heap, (-heap[right_idx], right_idx))

    return output

        


def main():

    nums = generate_random_list(50)
    nums = [-num for num in nums]
    heapq.heapify(nums)
    heap = [-num for num in nums]
    k = 10

    heap_copy = list(heap)
    heap_copy.sort(reverse=True)

    expected = heap_copy[:k]
    actual = compute_top_k_elements(heap, k)

    print("Expected:", expected)
    print("Actual:", actual)
main()

    



