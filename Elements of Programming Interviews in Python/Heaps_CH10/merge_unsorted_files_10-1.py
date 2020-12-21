# Write a program that takes as imput a set of sorted sequences and computes the union of these sequences as a sorted sequence.
# Ex. Input = [[3,5,7], [0,6], [0,6,28]] Output = [0,0,3,5,6,6,7,28]

from typing import List, Tuple, Iterable
import random
import heapq

def generate_random_test(max_num_lists: int) -> List[List[int]]:
    output = []
    for _ in range(max_num_lists):
        nums = []
        length = random.randint(2, 6)
        for __ in range(length):
            rand_num = random.randint(0, 100)
            nums.append(rand_num)
        output.append(sorted(nums))

    return output

def merge_sorted_arrays(sorted_arrs: List[List[int]]) -> List[int]:

    # Creates list of iter objs
    sorted_iters: [Iterable] = [iter(arr) for arr in sorted_arrs]
    
    # Create the min heap - each node is a tuple = (iter identifier, iter value)
    min_heap: List[Tuple(int, int)] = []

    for i, it in enumerate(sorted_iters):
        iter_val = next(it, None)
        if iter_val is not None:
            heapq.heappush(min_heap, (iter_val, i))

    output: List[int] = []
    while len(min_heap) > 0:
        # Get the min value from the heap and its associated iter id.
        iter_val, iter_id = heapq.heappop(min_heap)

        # Add the min value to the output list
        output.append(iter_val)

        # Get the iter object from the sorted iter list by the iter id.
        next_iter = sorted_iters[iter_id]

        # Get the next iter value from the identified sorted iter and add it to the heap if exists.
        next_iter_val = next(next_iter, None)
        if next_iter_val is not None:
            heapq.heappush(min_heap, (next_iter_val, iter_id))

    return output

def main():
    max_num_lists = 3
    nums = generate_random_test(max_num_lists)
    result = merge_sorted_arrays(nums)
    print(result)
main()