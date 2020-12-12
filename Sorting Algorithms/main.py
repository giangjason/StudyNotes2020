import sys
import time
from helper import Helper
from sort import Bubble, Selection, Insertion, Merge, Quick, Count

def main():

    low = -100000
    high = 100000
    length = 0

    args = sys.argv

    # nums = ([int(args[i]) for i in range(1, len(args))] if len(args) > 1 
    #             else Helper().generate_random_list(low, high, length))

    nums = []
    
    # BUBBLE SORT O(n2)
    print("\n")
    print("-----BUBBLE SORT------")
    bubble_nums = list(nums)
    if length <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Bubble().sort(bubble_nums)
    end = time.time()
    if length <= 25: print("Sorted numbers:", bubble_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # SELECTION SORT O(n2)
    print("\n")
    print("-----SELECTION SORT------")
    selection_nums = list(nums)
    if length <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Selection().sort(selection_nums)
    end = time.time()
    if length <= 25: print("Sorted numbers:", selection_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # INSERTION SORT O(n2)
    print("\n")
    print("-----INSERTION SORT------")
    insertion_nums = list(nums)
    if length <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Insertion().sort(insertion_nums)
    end = time.time()
    if length <= 25: print("Sorted numbers:", insertion_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # MERGE SORT O(n(logn))
    print("\n")
    print("-----MERGE SORT------")
    merge_nums = list(nums)
    if length <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Merge().sort(merge_nums)
    end = time.time()
    if length <= 25: print("Sorted numbers:", merge_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # QUICK SORT O(n(logn))
    print("\n")
    print("-----QUICK SORT------")
    quick_nums = list(nums)
    if length <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Quick().sort(quick_nums)
    end = time.time()
    if length <= 25: print("Sorted numbers:", quick_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # COUNT SORT O(n+k)
    print("\n")
    print("-----COUNT SORT------")
    count_nums = list(nums)
    if length <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Count().sort(count_nums)
    end = time.time()
    if length <= 25: print("Sorted numbers:", count_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    print("\n")

# if __name__ == "__main__":
#     main()

main()