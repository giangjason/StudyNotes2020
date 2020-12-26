# Design an algorithm that takes an array and sorts the array 
# so that all even numbers are on the left and odds on the right.

from typing import List
import random

def generate_random_list(length: int) -> List[int]:
    return [random.randint(0, 100) for _ in range(length)]

# def even_odd_array(nums: List[int]) -> None:
#     odd_idx = 0
#     even_idx = len(nums)-1
#     while odd_idx < even_idx:
#         # Look for the next odd number on the left
#         while odd_idx < len(nums) and nums[odd_idx] % 2 == 0:
#             odd_idx += 1
        
#         # Look for the next even number on the right
#         while even_idx > 0 and nums[even_idx] % 2 != 0:
#             even_idx -= 1

#         if odd_idx > even_idx:
#             break

#         # Swap the even and odd
#         nums[odd_idx], nums[even_idx] = nums[even_idx], nums[odd_idx]

def even_odd_array(nums: List[int]) -> None:
    even = 0
    odd = len(nums) - 1
    while even < odd:
        if nums[even] % 2 == 0:
            even += 1
        else:
            nums[even], nums[odd] = nums[odd], nums[even]
            odd -= 1

def main():
    length = 1
    nums = generate_random_list(length)
    print("Before:", nums)
    even_odd_array(nums)
    print("After:", nums)
main()
