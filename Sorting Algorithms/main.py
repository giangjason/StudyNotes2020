import sys
import time
from helper import Helper
from sort import Bubble, Selection, Insertion, Shell, Merge, Quick, Count, Radix, Bucket

def main():

    low = -99
    high = 99
    length = 20

    args = sys.argv

    nums = ([int(args[i]) for i in range(1, len(args))] if len(args) > 1 
                else Helper().generate_random_list(low, high, length))
    
    # BUBBLE SORT O(n2)
    print("\n")
    print("-----BUBBLE SORT------")
    bubble_nums = list(nums)
    if len(nums) <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Bubble().sort(bubble_nums)
    end = time.time()
    if len(nums) <= 25: print("Sorted numbers:", bubble_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # SELECTION SORT O(n2)
    print("\n")
    print("-----SELECTION SORT------")
    selection_nums = list(nums)
    if len(nums) <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Selection().sort(selection_nums)
    end = time.time()
    if len(nums) <= 25: print("Sorted numbers:", selection_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # INSERTION SORT O(n2)
    print("\n")
    print("-----INSERTION SORT------")
    insertion_nums = list(nums)
    if len(nums) <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Insertion().sort(insertion_nums)
    end = time.time()
    if len(nums) <= 25: print("Sorted numbers:", insertion_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # SHELL SORT O(n2)
    print("\n")
    print("-----SHELL SORT (LSD)------")
    shell_nums = list(nums)
    if len(nums) <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Shell().sort(shell_nums)
    end = time.time()
    if len(nums) <= 25: print("Sorted numbers:", shell_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # MERGE SORT O(n(logn))
    print("\n")
    print("-----MERGE SORT------")
    merge_nums = list(nums)
    if len(nums) <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Merge().sort(merge_nums)
    end = time.time()
    if len(nums) <= 25: print("Sorted numbers:", merge_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # QUICK SORT O(n(logn))
    print("\n")
    print("-----QUICK SORT------")
    quick_nums = list(nums)
    if len(nums) <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Quick().sort(quick_nums)
    end = time.time()
    if len(nums) <= 25: print("Sorted numbers:", quick_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # # COUNT SORT O(n+k)
    # print("\n")
    # print("-----COUNT SORT------")
    # count_nums = list(nums)
    # if len(nums) <= 25: print("Unsorted numbers:",nums)
    # start = time.time()
    # Count().sort(count_nums)
    # end = time.time()
    # if len(nums) <= 25: print("Sorted numbers:", count_nums)
    # print("Execution time: {0}ms".format((end-start)*1000))

    # # RADIX SORT O(d(n+k))
    # print("\n")
    # print("-----RADIX SORT------")
    # radix_nums = list(nums)
    # if len(nums) <= 25: print("Unsorted numbers:",nums)
    # start = time.time()
    # Radix().sort(radix_nums)
    # end = time.time()
    # if len(nums) <= 25: print("Sorted numbers:", radix_nums)
    # print("Execution time: {0}ms".format((end-start)*1000))

    # BUCKET SORT O(n+k)
    print("\n")
    print("-----BUCKET SORT------")
    bucket_nums = list(nums)
    if len(nums) <= 25: print("Unsorted numbers:",nums)
    start = time.time()
    Bucket().sort(bucket_nums)
    end = time.time()
    if len(nums) <= 25: print("Sorted numbers:", bucket_nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    print("\n")

main()

# if __name__ == "__main__":
#     main()

