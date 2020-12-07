from helper import Helper
from linear_search import LinearSearch

def main():

    helper = Helper()
    nums = helper.generate_ordered_list(0, 10)
    search_value = 0

    linear_search_result = LinearSearch().search(nums, search_value)
    print(linear_search_result)

main()
