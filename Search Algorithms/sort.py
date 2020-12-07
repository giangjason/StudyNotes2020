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
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

class SelectionSort():

    def sort(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n):
            low = i
            for j in range(i+1,n):
                if nums[j] < nums[low]:
                    low = j
            nums[low], nums[i] = nums[i], nums[low]
            
                

        
