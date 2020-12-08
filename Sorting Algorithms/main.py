import time
from helper import Helper
from sort import Bubble, Selection, Insertion, Merge

def main():

    helper = Helper()
    low = -100
    high = 100
    length = 25

    # BUBBLE SORT O(n2)
    print("\n")
    print("-----BUBBLE SORT------")
    nums = helper.generate_random_list(low, high, length)
    if length <= 25: print(nums)
    start = time.time()
    Bubble().sort(nums)
    end = time.time()
    if length <= 25: print("Sorted numbers:", nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # SELECTION SORT O(n2)
    print("\n")
    print("-----SELECTION SORT------")
    nums = helper.generate_random_list(low, high, length)
    if length <= 25: print(nums)
    start = time.time()
    Selection().sort(nums)
    end = time.time()
    if length <= 25: print("Sorted numbers:", nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # INSERTION SORT O(n2)
    print("\n")
    print("-----INSERTION SORT------")
    nums = helper.generate_random_list(low, high, length)
    if length <= 25: print(nums)
    start = time.time()
    Insertion().sort(nums)
    end = time.time()
    if length <= 25: print("Sorted numbers:", nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # MERGE SORT O(n(logn))
    print("\n")
    print("-----MERGE SORT------")
    nums = helper.generate_random_list(low, high, length)
    if length <= 25: print(nums)
    start = time.time()
    Merge().sort(nums)
    end = time.time()
    if length <= 25: print("Sorted numbers:", nums)
    print("Execution time: {0}ms".format((end-start)*1000))


    print("\n")

main()