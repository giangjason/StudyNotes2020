from typing import List


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
            nums[low], nums[i] = nums[i], nums[low]
            

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


        