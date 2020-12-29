from typing import List

# TODO: BucketSort
# TODO: CountSort with negative numbers
# TODO: Sorting with characters/strings


# Sorts a list by swapping adjacent elements if they are out of order. 
# This is done in multiple iterations until all elements are in the correct order. 
class Bubble():

    def sort(self, nums: List[int]) -> None:
        """Sorts a list by repeatedly steping through the list, 
        compares adjacent elements and swaps them if they are in the wrong order
        Time complexity: O(n2)
        Space complexity: O(1)
        
        Args:
            nums (List[int]): The list to sort.
        """
        n = len(nums)

        # Traverse through th list
        for i in range(n):
            for j in range(n-i-1):

                # Swap adjacent elements if they are out of order
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]


# Sorts a list by maintaining two sublists; sorted and a non-sorted. 
# Every iteration, the lowest element from the non-sorted sublist gets added 
# to the end of the sorted sublist until there are no remaining elements in the non-sorted sublist.
class Selection():

    def sort(self, nums: List[int]) -> None:
        """Sorts the list by maintaining two sublists - a sorted and non-sorted sublist. 
        The largest number in the unsorted sublist gets added to the end of the sorted sublist each iteration
        Time complexity: O(n2).
        Space complexity: O(1).

        Args:
            nums (List[int]): The list to sort
        """
        n = len(nums)
        for i in range(n):

            # Set the lowest to the beginning of the unsorted subarray
            low = i
            for j in range(i+1,n):

                # Find the lowest in the unsorted array
                if nums[j] < nums[low]:
                    low = j
            
            # Swap the beginning of the unsorted subarray and the lowest.
            # The beginning of the unsorted subarray now becomes the end of the sorted subarray
            nums[i], nums[low] = nums[low], nums[i]
            

# Sorts a list by maintaining two sublists; sorted and non-sorted. 
# Every iteration, the lowest element in the non-sorted sublist gets inserted into the correct
# position in the sorted sublist shifting elements to the right as needed.
class Insertion():

    def sort(self, nums: List[int]) -> None:
        """Sorts a list of numbers by inserting the lowest number into 
        the correct position of the sorted sublist.
        Time complexity: O(n2)
        Space complexity: O(1)

        Args:
            nums (List[int]): The list to sort
        """

        # Start at the 2nd element in the array
        for i in range(1, len(nums)):

            # Set the key to the beginning of the unsorted subarray
            key = nums[i]

            # Set a pointer to the end of the sorted subarray
            j = i-1

            # Shift elements in the sorted array to the right as needed
            # until the correct position for the key is found
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1

            # Set the key to the found position
            nums[j+1] = key


# Sorts a list by dividing the list in half each iteration, 
# sorting the halves, and combining the halves until the entire list is sorted.
class Merge():

    def sort(self, nums: List[int]) -> None:
        """Sorts a list by dividing the list in half each iteration, 
        sorting the halves, and combining the halves until the entire list is sorted.
        Time complexity: O(n(logn)).
        Space complexity: O(n) -> due to the stack used during recursion.

        Args:
            nums (List[int]): [description]
        """
        if len(nums) <= 1: return

        # Find the middle of the array
        mid = len(nums) // 2

        # Split the array elements into two halves
        left = nums[:mid]
        right = nums[mid:]

        # Sort the left half
        self.sort(left)

        # Sort the right half
        self.sort(right)

        # Merge the left and right arrays into the original array
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        # Add the remaining elements of the left array if any
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        # Add the remaining elements of the right array if any
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


# Sorts a list be defining a pivot and finding the position of the pivot in the list 
# where all elements to the left of the pivot are less than the pivot 
# and all elements to the right of the pivot are greater than the pivot.
class Quick():

    def _partition(self, nums: List[int], low: int, high: int) -> int:
        """Partitions an array so that elements less than the pivot are left of 
        the pivot and elements greater than the pivot are right of the pivot.

        Args:
            low (int): The lower bound of the array to partition.
            high (int): The upper bound of the array to partition.
            nums (List[int]): The array to partition.

        Returns:
            int: The indexed position of the pivot.
        """

        # Set the pivot as the last element in the list
        p = nums[high]

        # Set the position for the pivot's final resting place 
        # (the end of the subarray where elements are less than the pivot)
        i = low-1

        # Traverse the arraym swap i and j whenever encountering an element less than the pivot
        for j in range(low, high):
            if nums[j] <= p:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        # Set the pivot between the subarray that contains elements lower and the subarray that contains elements higher.
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i+1

    def _sort(self, nums: List[int], low: int, high: int) -> None:
        if low >= high: return

        # Determine the position of the pivot
        p = self._partition(nums, low, high)

        # Sort the subarray left of the pivot (contains elements less than the pivot)
        self._sort(nums, low, p-1)

        # Sort the subarray right of the pivot (contains elements greater than the pivot)
        self._sort(nums, p+1, high)

    def sort(self, nums: List[int]) -> None:
        self._sort(nums, 0, len(nums)-1)

            
# Sorts an array by calculating the number of occurances of an element in the array and setting 
# the position of each element based on the position derived from the occurance count.
# The array MUST be contain only positive integers. 
# Time complexity: O(n+k) where n = the array and k = the maximum number in the array.
class Count():

    def sort(self, nums: List[int]) -> None:
        """Sorts an array by the number of occurances of each element in the array.
        Must contain only positive integers. 
        Time complexity: O(n+k)
        Space complexity: O(n+k)

        Args:
            nums (List[int]): [description]
        """
        size = len(nums)

        # Determine the max number in the array
        max_num = 0
        for num in nums:
            if num > max_num:
                max_num = num

        # Initialize the count array
        count = [0] * (max_num+1)

        # Store the number of occurances in the array into the count array (O(n))
        for i in range(size):
            count[nums[i]] += 1

        # Calculate the accumulative sum in the count array (O(k))
        for j in range(1, len(count)):
            count[j] += count[j-1]

        # Sort the numbers in the array based on the count position in the count array (O(n))
        output = [0] * size
        h = size-1
        while h >= 0:
            key = nums[h]
            index = count[key]-1
            output[index] = key
            count[key] -= 1
            h -= 1

        # Copy the output into the array
        for l in range(size):
            nums[l] = output[l]

# Sorts the elements in an array by first grouping the individual digits of the same place value. 
# Then, sort the elements according to their increasing/decreasing order. 
# Below is a representation of Radix sort using the least significant digit (LSD)
class Radix():

    def sort(self, nums: List[int]) -> None:
        
        # Get the maximum element in the array
        max_num = 0
        for num in nums:
            if num > max_num:
                max_num = num

        # Count sort the array based on the current place of the digit
        place = 1
        while max_num // place > 0:
            self._count_sort(nums, place)
            place *= 10

    def _count_sort(self, nums: List[int], place: int) -> None:
        
        # Get the size of the array
        size = len(nums)
        
        # Initialize the count - (we are only initializing a 10sized array because we are working with singular digits (0-9))
        count = [0] * 10

        # Calculate the occurances of an element and store in the count array
        for i in range(size):
            
            # Get the place of the current number
            num = nums[i] // place

            # Get the digit of the place to be used as the index
            index = num % 10
            count[index] += 1

        # Calculated the accumulative sum of the occurances
        for j in range(1, len(count)):
            count[j] += count[j-1]

        # Sort the array into a new output array based on the positions determined in the count array
        output = [0] * size
        h = size - 1
        while h >= 0:
            num = nums[h] // place
            index = count[num % 10]-1
            output[index] = nums[h]
            count[num % 10] -= 1
            h -= 1

        # Copy the output array into the original array
        for h in range(size):
            nums[h] = output[h]

class Shell():

    def sort(self, nums: List[int]) -> None:
        n = len(nums)
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                num = nums[i]
                j = i
                while j >= interval and nums[j - interval] > num:
                    nums[j] = nums[j - interval]
                    j -= interval

                nums[j] = num
            interval //= 2

