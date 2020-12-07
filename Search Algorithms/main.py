import timeit
from helper import Helper
from search import (LinearSearch, BinarySearch, 
                        ExponentialSearch, InterpolationSearch)

def main():

    show_recursion = True

    start_num = 1
    length = 100
    search_value = 37

    helper = Helper()
    nums = helper.generate_ordered_list(start_num, length)

    if len(nums) < 15:
        print("\n")
        print("Numbers generated:", nums)

    # LINEAR SEARCH O(n)
    print("\n")
    print("-----LINEAR SEARCH O(n)-----")
    start = timeit.timeit()
    result = LinearSearch().search(nums, search_value)
    end = timeit.timeit()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format(end-start))

    # BINARY SEARCH O(logn)
    print("\n")
    print("-----BINARY SEARCH O(logn)-----")
    start = timeit.timeit()
    result = BinarySearch().search(nums, search_value)
    end = timeit.timeit()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format(end-start))

    if show_recursion:
        # BINART SEARCH RECURSIVE O(logn)
        print("\n")
        print("-----BINARY SEARCH RECURSIVE O(logn)-----")
        start = timeit.timeit()
        result = BinarySearch().search_recursive(nums, search_value)
        end = timeit.timeit()
        print("Contains value: ({0})? ({1})".format(search_value, result))
        print("Execution time: {0}ms".format(end-start))

    # EXPONENTIAL SEARCH O(logn)
    print("\n")
    print("-----EXPONENTIAL SEARCH O(logn)-----")
    start = timeit.timeit()
    result = ExponentialSearch().search(nums, search_value)
    end = timeit.timeit()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format(end-start))

    # INTERPOLATION SEARCH O(log(logn))
    print("\n")
    print("-----INTERPOLATION SEARCH O(logn)-----")
    start = timeit.timeit()
    result = InterpolationSearch().search(nums, search_value)
    end = timeit.timeit()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format(end-start))


    print("\n")
main()
