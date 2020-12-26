# Design an algo that sorts an array that contains increasing and decreasing elements
# Ex. [57, 131, 493, 24, 221, 339, 418, 452, 442, 190]

from typing import List, Tuple, Iterable
import heapq

def decompose_list(nums: List[int]) -> List[List[int]]:
    output, inc, dec = [], [], []
    i = 0
    for j in range(1, len(nums)):
        
        # If the next number is increasing and the decreasing list is empty,
        # this means i is in the middle of an increasing range. 
        # Add the number at i to the increasing list.
        if nums[j] > nums[i] and not dec:
            inc.append(nums[i])

        # If the next number is increasing and the decreasing list is not empty,
        # this means i is at the end of a decreasing range and the increasing range is starting.
        # Add the the number at i to the increasing list and add the decreasing list to 
        # the output. Reset the decreasing list.
        elif nums[j] > nums[i] and dec:
            inc.append(nums[i])
            dec.reverse()
            output.append(dec)
            dec = []

        # If the next number is decreasing and the increasing list is empty,
        # this means i is in the middle of a decreasing range.
        # Add the number at i to the decreasing list.
        elif nums[j] < nums[i] and not inc:
            dec.append(nums[i])

        # If the next number is decreasing and the increasing list is not empty,
        # this means i is at the end of an increasing range and the decreasing range is starting.
        # Add the the number at i to the decreasing list and add the increasing list to 
        # the output. Reset the increasing list.
        elif nums[j] < nums[i] and inc:
            dec.append(nums[i])
            output.append(inc)
            inc = []

        i += 1

    # Add last item in the array to either inc or dec list.
    if inc: 
        inc.append(nums[i])
        output.append(inc)
    else: 
        dec.append(nums[i])
        dec.reverse()
        output.append(dec)

    return output

def merge_sorted_arrays(nums: List[List[int]]) -> List[int]:
    sorted_iters: List[Iterable] = [iter(i) for i in nums]
    heap: List[Tuple(int, int)] = []
    for it_id, it in enumerate(sorted_iters):
        it_val = next(it, None)
        if it_val is not None:
            heapq.heappush(heap, (it_val, it_id))

    output = []
    while len(heap) > 0:
        smallest_it = heapq.heappop(heap)
        smallest_it_val = smallest_it[0]
        smallest_it_id = smallest_it[1]
        output.append(smallest_it_val)
        next_it = sorted_iters[smallest_it_id]
        next_it_val = next(next_it, None)
        if next_it_val is not None:
            heapq.heappush(heap, (next_it_val, smallest_it_id))

    return output




def main():
    nums = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
    list_of_numlists = decompose_list(nums)
    merged_nums = merge_sorted_arrays(list_of_numlists)
    print(merged_nums)
main()