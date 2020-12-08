import unittest
from listnode import ListNode
from helper import Helper
from mergeTwoSortedLists import Solution

class Test_MergeTwoSortedLists(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_one(self):
        nums1 = [1,2,4]
        nums2 = [1,3,4]

        l1 = Helper.construct_linked_list(nums1)
        l2 = Helper.construct_linked_list(nums2)

        result = self.solution.mergeTwoLists(l1, l2)
        result_arr = Helper.convert_to_array(result)

        self.assertEqual(result_arr, [1,1,2,3,4,4])

    def test_two(self):
        nums1 = []
        nums2 = []

        l1 = Helper.construct_linked_list(nums1)
        l2 = Helper.construct_linked_list(nums2)

        result = self.solution.mergeTwoLists(l1, l2)
        result_arr = Helper.convert_to_array(result)

        self.assertEqual(result_arr, [])

    def test_three(self):
        nums1 = []
        nums2 = [0]

        l1 = Helper.construct_linked_list(nums1)
        l2 = Helper.construct_linked_list(nums2)

        result = self.solution.mergeTwoLists(l1, l2)
        result_arr = Helper.convert_to_array(result)

        self.assertEqual(result_arr, [0])

    def test_four(self):
        nums1 = [0]
        nums2 = []

        l1 = Helper.construct_linked_list(nums1)
        l2 = Helper.construct_linked_list(nums2)

        result = self.solution.mergeTwoLists(l1, l2)
        result_arr = Helper.convert_to_array(result)

        self.assertEqual(result_arr, [0])

    def test_five(self):
        nums1 = [-1,0,4,6,12,20]
        nums2 = [-9,2,6,8,30]

        l1 = Helper.construct_linked_list(nums1)
        l2 = Helper.construct_linked_list(nums2)

        result = self.solution.mergeTwoLists(l1, l2)
        result_arr = Helper.convert_to_array(result)

        self.assertEqual(result_arr, [-9,-1,0,2,4,6,6,8,12,20,30])

if __name__ == '__main__':
    unittest.main()



 
