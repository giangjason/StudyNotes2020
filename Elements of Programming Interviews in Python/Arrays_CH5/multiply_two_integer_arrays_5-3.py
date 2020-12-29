# Write a program that accepts two arrays representing two integers and returns an array representing their product
# Ex.1 input = [1,2,3], [2,3] output = [2,8,2,9]

from helper import Helper
from typing import List
import random
import sys

def multiple_two_interger_arrays(num1: List[int], num2: List[int]) -> List[int]:
    return []
    
def main():
    h = Helper()

    args = sys.argv
    if len(args) > 1:
        num1 = [int(digit) for digit in list(args[1])]
        num2 = [int(digit) for digit in list(args[2])]
    else:
        low, high, length = 0, 9, 4
        num1 = h.generate_random_list(low, high, length)
        num2 = h.generate_random_list(low, high, length)

    print("Num1:", num1)
    print("Num2:", num2)
    
    tmp = str(int(''.join([str(digit) for digit in num1])) * int(''.join([str(digit) for digit in num2])))
    expected = [int(digit) for digit in tmp]
    actual = multiple_two_interger_arrays(num1, num2)  

    print("Expected:", expected)
    print("Actual:", actual)
main()
    
