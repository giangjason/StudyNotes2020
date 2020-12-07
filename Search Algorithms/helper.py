from typing import List
import random

class Helper():

    def generate_ordered_list(self, start: int, length: int) -> List[int]:
        """Generates and returns an ordered list of numbers

        Args:
            start (int): The starting number of the list
            length (int): The length of the list

        Returns:
            List[int]: An ordered list of numbers
        """
        nums = []
        for i in range(start, start+length+1):
            nums.append(i)
        return nums

    
    def copy_nums(self, nums: List[int]) -> List[int]:
        """Copies and returns a new list containing the numbers from the given list.

        Args:
            nums (List[int]): The list of numbers to copy from.

        Returns:
            List[int]: A new list of copied numbers.
        """
        return List(nums)