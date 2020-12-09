import unittest
from listnode import ListNode
from helper import Helper
from reverseLinkedList import Solution

class Test_ReverseLinkedList(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_one(self):
        nums = [1,2,3,4,5]

        head = Helper.construct_linked_list(nums)

        result = self.solution.reverseList(head)
        result_arr = Helper.convert_to_array(result)

        self.assertIsNotNone(result)
        self.assertEqual(result_arr, [5,4,3,2,1])

    def test_two(self):
        nums = [0]

        head = Helper.construct_linked_list(nums)

        result = self.solution.reverseList(head)
        result_arr = Helper.convert_to_array(result)

        self.assertIsNotNone(result)
        self.assertEqual(result_arr, [0])

    def test_three(self):
        nums = []

        head = Helper.construct_linked_list(nums)

        result = self.solution.reverseList(head)
        result_arr = Helper.convert_to_array(result)

        self.assertEqual(result_arr, [])

if __name__ == "__main__":
    unittest.main()