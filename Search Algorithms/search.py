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
    
class BinarySearch():

    def search(self, nums: List[int], val: int) -> bool:
        """Searches for a given value by halving the list each iteration until 
        the value is found or there is only one number left in the list. 
        This method searches iteratively.
        Time complexity: O(logn)

        Args:
            nums (List[int]): The list of numbers to search
            val (int): The value to search for

        Returns:
            bool: True if found, False if now.
        """
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (high+low)//2

            if nums[mid] == val:
                return True
            elif nums[mid] < val:
                low = mid + 1
            else:
                high = mid - 1
            
        return False
    
    def search_recursive(self, nums: List[int], val: int) -> bool:
        """Searches for a given value by halving the list each iteration until 
        the value is found or there is only one number left in the list. 
        This method searches recursively.
        Time complexity: O(logn)

        Args:
            nums (List[int]): The list of numbers to search
            val (int): The value to search for

        Returns:
            bool: True if found, False if now.
        """
        low = 0
        high = len(nums)-1

        def _search(low: int, high: int) -> bool:
            if low > high:
                return False

            mid = (low+high)//2
            if nums[mid] == val:
                return True
            elif nums[mid] < val:
                return _search(mid+1, high)
            else:
                return _search(low, high-1) 
        
        return _search(low, high)