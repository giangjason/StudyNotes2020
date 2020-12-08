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
            low = i
            for j in range(i+1,n):
                if nums[j] < nums[low]:
                    low = j
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

        # Traverse through the list
        for i in range(1, len(nums)):

            # Get the element at the 1st index
            key = nums[i]

            # Move elements of arr[0..i-1], that are 
            # greater than key, to one position ahead 
            # of their current position 
            j = i-1
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1

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
        if len(nums) > 1:

            # Find the middle of the array
            mid = len(nums) // 2

            # Split the array elements into two halves
            left = nums[:mid]
            right = nums[mid:]

            # Sort the left half
            self.sort(left)

            # Sort the right half
            self.sort(right)

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


        
