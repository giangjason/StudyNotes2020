import sys
import time
from helper import Helper
from search import Linear, Binary, Exponential, Interpolation

def main():
    show_recursion = False
    
    if len(sys.argv) > 2:
        search_value = int(sys.argv[1])
        nums = []
        for i in range(2, len(sys.argv)):
            nums.append(int(sys.argv[i]))
    else:
        start_num = 1
        length = 10
        search_value = 87
        nums = Helper().generate_ordered_list(start_num, length)

    if len(nums) < 15:
        print("\n")
        print("-----Numbers generated------\n", nums)

    # LINEAR SEARCH O(n)
    print("\n")
    print("-----LINEAR SEARCH O(n)-----")
    start = time.time()
    result = Linear().search(nums, search_value)
    end = time.time()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format((end-start)*1000))

    # BINARY SEARCH O(logn)
    print("\n")
    print("-----BINARY SEARCH O(logn)-----")
    start = time.time()
    result = Binary().search(nums, search_value)
    end = time.time()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format((end-start)*1000))

    if show_recursion:
        # BINART SEARCH RECURSIVE O(logn)
        print("\n")
        print("-----BINARY SEARCH RECURSIVE O(logn)-----")
        start = time.time()
        result = Binary().search_recursive(nums, search_value)
        end = time.time()
        print("Contains value: ({0})? ({1})".format(search_value, result))
        print("Execution time: {0}ms".format((end-start)*1000))

    # EXPONENTIAL SEARCH O(logn)
    print("\n")
    print("-----EXPONENTIAL SEARCH O(logn)-----")
    start = time.time()
    result = Exponential().search(nums, search_value)
    end = time.time()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format((end-start)*1000))

    # INTERPOLATION SEARCH O(log(logn))
    print("\n")
    print("-----INTERPOLATION SEARCH O(logn)-----")
    start = time.time()
    result = Interpolation().search(nums, search_value)
    end = time.time()
    print("Contains value: ({0})? ({1})".format(search_value, result))
    print("Execution time: {0}ms".format((end-start)*1000))


    print("\n")


if __name__ == "__main__":
    main()