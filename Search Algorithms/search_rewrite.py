from typing import List

class LinearSearch():

    def search(self, nums: List[int], val: int) -> bool:
        for num in nums:
            if num == val:
                return True
        return False


class BinarySearch():

    def search(self, nums: List[int], val: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high: 
            mid = (low + high) // 2

            if nums[mid] == val:
                return True
            elif nums[mid] < val: 
                low = mid + 1 
            else:
                high = mid - 1
        
        return False
    
    def search_recursive(self, nums: List[int], val: int) -> bool:

        def _search(low: int, high: int) -> bool:
            if low > high:
                return False

            mid = (low + high) // 2
            if nums[mid] == val:
                return True
            elif nums[mid] < val: 
                return _search(mid + 1, high)
            else:
                return _search(low, mid-1)
        
        low = 0
        high = len(nums) - 1
        return _search(low, high)


class ExponentialSearch():

    def search(self, nums: List[int], val: int) -> bool:
        if len(nums) == 0:
            return False

        if nums[0] == val:
            return True
        
        i = 1
        n = len(nums) - 1
        while i <= n and nums[i] <= val:
            i *= 2
        
        low = i // 2
        high = i if i < n else n
        return BinarySearch().search(nums[low:high+1], val)


class InterpolationSearch():

    def search(self, nums: List[int], val: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high and nums[low] <= val and nums[high] >= val:
            pos = low + ((val - nums[low]) * (high - low) // (nums[high] - nums[low]))

            if nums[pos] == val:
                return True
            elif nums[pos] < val:
                low = pos + 1
            else:
                high = pos - 1

        return False




