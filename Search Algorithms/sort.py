from typing import List

class BubbleSort():

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

class SelectionSort():

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
            

class InsertionSort():

    def sort(self, nums: List[int]) -> None:
        """Sorts a list of numbers by inserting the lowest number into the front each iteration.
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



        
