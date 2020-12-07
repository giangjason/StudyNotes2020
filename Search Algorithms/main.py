import time
import data
from helper import Helper
from search import LinearSearch, BinarySearch, ExponentialSearch, InterpolationSearch
from sort import BubbleSort, SelectionSort

def run_sort():
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
    BubbleSort().sort(nums)
    end = time.time()
    if length <= 25: print("Sorted numbers:", nums)
    print("Execution time: {0}ms".format((end-start)*1000))

    # SELECTION SORT O(n2)
    print("\n")
    print("-----SELECTION SORT------")
    nums = helper.generate_random_list(low, high, length)
    if length <= 25: print(nums)
    start = time.time()
    SelectionSort().sort(nums)
    end = time.time()
    if length <= 25: print("Sorted numbers:", nums)
    print("Execution time: {0}ms".format((end-start)*1000))


    print("\n")


def run_search():
    show_recursion = True

    start_num = 1
    length = 100000000
    search_value = 921200007687687

    helper = Helper()
    nums = helper.generate_ordered_list(start_num, length)

    if len(nums) < 15:
        print("\n")
        print("Numbers generated:", nums)

    # LINEAR SEARCH O(n)
    print("\n")
    print("-----LINEAR SEARCH O(n)-----")
    start = time.time()
    result = LinearSearch().search(nums, search_value)
    end = time.time()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format((end-start)*1000))

    # BINARY SEARCH O(logn)
    print("\n")
    print("-----BINARY SEARCH O(logn)-----")
    start = time.time()
    result = BinarySearch().search(nums, search_value)
    end = time.time()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format((end-start)*1000))

    if show_recursion:
        # BINART SEARCH RECURSIVE O(logn)
        print("\n")
        print("-----BINARY SEARCH RECURSIVE O(logn)-----")
        start = time.time()
        result = BinarySearch().search_recursive(nums, search_value)
        end = time.time()
        print("Contains value: ({0})? ({1})".format(search_value, result))
        print("Execution time: {0}ms".format((end-start)*1000))

    # EXPONENTIAL SEARCH O(logn)
    print("\n")
    print("-----EXPONENTIAL SEARCH O(logn)-----")
    start = time.time()
    result = ExponentialSearch().search(nums, search_value)
    end = time.time()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format((end-start)*1000))

    # INTERPOLATION SEARCH O(log(logn))
    print("\n")
    print("-----INTERPOLATION SEARCH O(logn)-----")
    start = time.time()
    result = InterpolationSearch().search(nums, search_value)
    end = time.time()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format((end-start)*1000))


    print("\n")


def main():

    show_search = False
    show_sort = True

    if show_search: run_search()
    if show_sort: run_sort()
    
main()