from typing import List

class LinearSearch():

    def search(self, nums: List[int], val: int) -> bool:
        """Searches a list one by one in order 
        from left to right for the given value. 
        Time complexity: O(n)

        Args:
            nums (List[int]): The list of numbers to search
            val (int): The value to search for

        Returns:
            bool: True if found, False if not.
        """
        for num in nums:
            if num == val:
                return True
        return False