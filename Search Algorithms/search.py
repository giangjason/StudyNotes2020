from typing import List


# Searches a collection of items one by one, in a sequential fashion.
class Linear():

    def search(self, nums: List[int], val: int) -> bool:
        """Searches a list one by one in order 
        from left to right for the given value. 
        Time complexity: O(n)
        Space complexity: O(1)

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


# Searches a collection of items by halving the collection of items each iterations. 
# Each iteration defines a sub-collection that is half the previous collection.  
class Binary():

    def search(self, nums: List[int], val: int) -> bool:
        """Searches for a given value by halving the list each iteration until 
        the value is found or there is only one number left in the list. 
        This method searches iteratively.
        Time complexity: O(logn)
        Space complexity: O(1)

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
        Space complexity: O(logn)

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
                return _search(low, mid-1) 
        
        return _search(low, high)


# A search that first finds a range of the collection to search in by doubling the range 
# each iteration until the high bound of the iteration is either at or above search target.
# The defined range then undergoes a binary search.
class Exponential():

    def search(self, nums: List[int], val: int) -> bool:
        """Searches a collection by first defining a range by doubling an upperbound each iteration. 
        The range then undergoes binary search. 
        Time complexity: O(logn) 
        Space complexity: O(1)  

        Args:
            nums (List[int]): The numbers to search.
            val (int): The target to search for.

        Returns:
            int: The position of the found value. -1 if not found.
        """
        if nums[0] == val:
            return True

        i = 1
        while i < len(nums) and nums[i] <= val:
            i *= 2
        
        lower = i//2
        upper = i if i < len(nums)-1 else len(nums)-1

        return Binary().search(nums[lower : upper+1], val)


# Searches a collection by first determining a lower and upper bound. 
# The lower and upper bounds are used to determine position (pos). 
# The lower bound, upper bound, and position are recalculated each iteration 
# until the element is found or until the lower and upper bound cross.
class Interpolation():

    def search(self, nums: List[int], val: int) -> bool:
        """Searches a collection by first determining the closest 
        position in the collection to the item being searched.
        Time complexity: O(log(logn))

        Args:
            nums (List[int]): The numbers to search.
            val (int): The value to search for.

        Returns:
            bool: True if found, False if not.
        """

        low = 0
        high = len(nums) - 1
        
        while low <= high and val >= nums[low] and val <= nums[high]:
            pos = low + ((val - nums[low]) * (high - low) // (nums[high] - nums[low]))

            if nums[pos] == val:
                return True
            elif nums[pos] < val:
                low = pos + 1
            else:
                high = pos - 1

        return False


