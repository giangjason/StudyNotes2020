# Write a program that takes in an array representing an integer number and adds 1 to it. 
# Ex.1 input = [1,3,1] output = [1,3,2]
# Ex.2 input = [9,9,9] output = [1,0,0,0]

from typing import List
import random
import sys

def generate_random_list(digits: int) -> List[int]:
    return [random.randint(1,9) for _ in range(digits)]

def increment_interger_array(arr: List[int]) -> List[int]:
    n = len(arr)-1
    arr[n] += 1
    place = 0
    for i in range(n, -1, -1):
        arr[i] += place
        place = arr[i] // 10
        arr[i] %= 10
        if place == 0:
            return

    if place > 0:
        return [place] + arr
    return arr

def main():

    args = sys.argv
    if len(args) > 1:
        tmp = list(args[1])
        nums = [int(digit) for digit in tmp]
    else:
        digits = 3
        nums = generate_random_list(digits)

    print("Before:", nums)
    plus_one = increment_interger_array(nums)
    print("After:", plus_one)

main()
