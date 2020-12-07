import timeit
from helper import Helper
from search import LinearSearch, BinarySearch

def main():

    start_num = 1
    length = 10000
    search_value = 99999

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
    print("Execution time: {0}ms".format(start-end))

    # BINART SEARCH O(logn)
    print("\n")
    print("-----BINARY SEARCH O(logn)-----")
    start = timeit.timeit()
    result = BinarySearch().search(nums, search_value)
    end = timeit.timeit()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format(start-end))

    if length < 100000:
        # BINART SEARCH RECURSIVE O(logn)
        print("\n")
        print("-----BINARY SEARCH RECURSIVE O(logn)-----")
        start = timeit.timeit()
        result = BinarySearch().search_recursive(nums, search_value)
        end = timeit.timeit()
        print("Contains value: ({0})? ({1})".format(search_value, result))
        print("Execution time: {0}ms".format(start-end))


    print("\n")
main()
