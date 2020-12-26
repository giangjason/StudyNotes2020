# Design an algorithm to compute the running median of a sequence of numbers. 
# The sequence is presented to you in a streaming fashion - you can not backup to read an earlier value 
# and you need to output the median after reading in each new element. 
# Ex. input = 1, 0, 3, 5, 2, 0, 1 output = 1, 0.5, 1, 2, 2, 1.5, 1

from typing import List, Iterator
import random
import statistics
import heapq

def generate_random_list(length: int) -> List[int]:
    return [random.randint(0, 100) for _ in range(length)]

def check_test_case(nums: List[int]):
    output = []
    for i in range(1, len(nums)+1):
        sub_num = nums[:i]
        median = statistics.median(sub_num)
        output.append(median)
    return output

# def compute_running_median(nums_iter: Iterator[int]) -> List[float]:
#     output, left, right = [], [], []
#     num = next(nums_iter, None)
#     while num is not None:
#         # Add to the right and get the min val from the right
#         right_min = heapq.heappushpop(right, num)

#         # Add the right min to the left
#         heapq.heappush(left, -right_min)

#         # Balance the left and right heaps
#         if len(left) > len(right):
#             left_max = -heapq.heappop(left)
#             heapq.heappush(right, left_max)

#         if len(left) == len(right):
#             median = (-left[0] + right[0]) / 2
#         else:
#             median = right[0]

#         output.append(median)
#         num = next(nums_iter, None)

#     return output

def compute_running_median(nums_iter: Iterator[int]) -> List[float]:
    output, left, right = [], [], []
    num = next(nums_iter, None)
    while num is not None:
        # Add to the left and get the max from the left
        left_max = -heapq.heappushpop(left, -num)

        # Add the left max to the right
        heapq.heappush(right, left_max)

        # Balance the left and right
        if len(right) > len(left):
            right_min = heapq.heappop(right)
            heapq.heappush(left, -right_min)

        if len(right) == len(left):
            median = (-left[0] + right[0]) / 2
        else:
            median = -left[0]

        output.append(median)
        num = next(nums_iter, None)

    return output


def main():
    nums = [1, 0, 3, 5, 2, 0, 1]
    expected = check_test_case(nums)
    actual = compute_running_median(iter(nums))
    print("Expected:", expected)
    print("Actual:", actual)
main()
