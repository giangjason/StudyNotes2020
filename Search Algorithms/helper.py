from typing import List
import random

class Helper():

    def generate_random_list(self, low: int, high: int, nums_length: int) -> List[int]:
        """ Generates and returns a list of randomly generated numbers

        Args:
            low (int): The lowest possible number generated.
            high (int): The highest possible number generated.
            nums_length (int): The length of the list.

        Returns:
            List[int]: A list containing randomly generated numbers.
        """
        nums = []
        for i in range(nums_length):
            nums.append(random.randint(low, high))
        return nums

    def generate_ordered_list(self, low: int, high: int) -> List[int]:
        """Generates and returns an ordered list of numbers

        Args:
            low (int): The lowest value in the list
            high (int): The highest value in the list

        Returns:
            List[int]: An ordered list of numbers
        """
        nums = []
        for i in range(low, high+1):
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