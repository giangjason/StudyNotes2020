# Write a program that accepts two arrays representing two integers and returns an array representing their product
# Ex.1 input = [1,2,3], [2,3] output = [2,8,2,9]

from typing import List
import random
import sys

def generate_random_list() -> List[int]:
    nums = [random.randint(1, 9) for _ in range(random.randint(2,9))]
    neg = random.randint(1,2) % 2 == 0
    if neg:
        nums[0] *= -1
    return nums

def multiple_two_interger_arrays(num1: List[int], num2: List[int]) -> List[int]:
    if len(num2) > len(num1):
        num1, num2 = num2, num1

    product = 0
    for i in range(len(num2)-1, -1, -1):
        subproduct = 0
        extra = 0
        for j in range(len(num1)-1, -1, -1):
            subproduct *= 10
            subproduct += num2[i] * num1[j] + extra
            extra = subproduct // 10
            subproduct %= 10
        product *= 10
        product += subproduct





    
def main():
    args = sys.argv
    if len(args) > 1:
        num1 = [int(digit) for digit in list(args[1])]
        num2 = [int(digit) for digit in list(args[2])]
    else:
        num1 = generate_random_list()
        num2 = generate_random_list()

    print("Num1:", num1)
    print("Num2:", num2)
    print("Product:", [])
main()
    
