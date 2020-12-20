from helper import Helper
import sys

class MaxHeap():

    def __init__(self):
        self.heap = []

    def insert(self, val: int) -> None:
        """Inserts an element into the heap and sorts itself to maintain max-heap properties.

        Time complexity:
            Average: O(logn)
            Worst: O(logn)

        Args:
            val (int): The value to insert.
        """
        # Insert at the end
        self.heap.append(val)

        # Determine the index positions of the current element and its parent.
        curr_idx = len(self.heap)-1
        parent_idx = (curr_idx - 1) // 2
        
        # Repeatedly swap the current element with its parent if the parent is smaller.
        while parent_idx >= 0 and self.heap[parent_idx] < self.heap[curr_idx]:
            self.heap[parent_idx], self.heap[curr_idx] = self.heap[curr_idx], self.heap[parent_idx]
            curr_idx = parent_idx
            parent_idx = (curr_idx - 1) // 2
        

    def delete(self, val: int) -> None:
        """Deletes an item from the heap

        Time complexity:
            Average: O(logn)
            Worst: O(logn)

        Args:
            val (int): The value to delete.
        """
        
        # Determine the indexed position of the element to delete.
        try:
            curr_idx = self.heap.index(val)
        except:
            # Return out of the heap does not contain the element to delete
            return

        # Replace the element to delete with the last element in the heap
        self.heap[curr_idx] = self.heap[-1]

        # Remove the last element in the heap
        self.heap.pop()

        # Sort the heap
        self._heapify(curr_idx)
        

    def get_max(self) -> int:
        """Gets the max element in the heap.

        Time complexity:
            Retrieval: O(1)
            Heapify: O(logn)

        Returns:
            int: The max element.
        """
        # Get the first item in the heap
        max_val = self.heap[0]

        # Replace the first item with the last item in the heap
        self.heap[0] = self.heap[-1]

        # Remove the last item in the heap
        self.heap.pop()
        
        # Sort the heap
        self._heapify()

        return max_val


    def search(self, val: int) -> bool:
        """Searches the heap for an element.

        Time complexity:
            Average: O(n)
            Worst: O(n)

        Args:
            val (int): The value to search for

        Returns:
            bool: True if found, False if not in heap.
        """
        for num in self.heap:
            if num == val:
                return True
        return False

    def _heapify(self, curr_idx: int = 0) -> None:
        """Sorts the heap by swapping parent and children if the parent is less than any of the children.

        Time complexity:
            Average: O(logn)

        Args:
            curr_idx (int, optional): The indexed position of the starting parent. Defaults to 0.
        """ 
        heap_size = len(self.heap)
        # Determine the left and right children
        left_idx = 2 * curr_idx + 1
        right_idx = 2 * curr_idx + 2

        # Repeatedly swap the current element with its children if the current element is smaller than its children
        while (left_idx < heap_size or right_idx < heap_size 
            and (self.heap[curr_idx] < self.heap[left_idx] or self.heap[curr_idx] < self.heap[right_idx])):

            # Swap with the larger child if both children are larger
            if (left_idx < heap_size and right_idx < heap_size) and (self.heap[left_idx] > self.heap[curr_idx] and self.heap[right_idx] > self.heap[curr_idx]):
                if self.heap[left_idx] > self.heap[right_idx]:
                    self.heap[curr_idx], self.heap[left_idx] = self.heap[left_idx], self.heap[curr_idx]
                    curr_idx = left_idx
                else:
                    self.heap[curr_idx], self.heap[right_idx] = self.heap[right_idx], self.heap[curr_idx]
                    curr_idx = right_idx
            # Swap with the left child if the left child is larger
            elif left_idx < heap_size and self.heap[left_idx] > self.heap[curr_idx]:
                self.heap[curr_idx], self.heap[left_idx] = self.heap[left_idx], self.heap[curr_idx]
                curr_idx = left_idx
            # Swap with the right child if the right child is larger
            elif right_idx < heap_size and self.heap[right_idx] > self.heap[curr_idx]:
                self.heap[curr_idx], self.heap[right_idx] = self.heap[right_idx], self.heap[curr_idx]
                curr_idx = right_idx

            left_idx = 2 * curr_idx + 1
            right_idx = 2 * curr_idx + 2

            
            

def main():

    low = 0
    high = 1000
    length = 20
    
    helper = Helper()
    args = sys.argv
    if len(args) > 1:
        nums = [int(arg) for arg in args[1:]]
    else:
        nums = helper.generate_random_list(low, high, length)

    print("\n")
    print("-----Numbers Generated-----")
    print(nums)

    print("\n")
    print("-----Max Heap-----")
    heap = MaxHeap()
    for num in nums:
        heap.insert(num)
    print(heap.heap)
    root = helper.construct_binary_tree(heap.heap)
    print(root)

    print("\n")
    print("-----Retrieving Max-----")
    max_val = heap.get_max()
    print("Max item:", max_val)
    print("Heap after retrieval:")
    print(heap.heap)
    root = helper.construct_binary_tree(heap.heap)
    print(root)

    print("\n")
    mid_idx = len(heap.heap) // 4
    mid_num = heap.heap[mid_idx]
    print("-----Deleting {0}-----".format(mid_num))
    heap.delete(mid_num)
    print("Heap after deletion:")
    print(heap.heap)
    root = helper.construct_binary_tree(heap.heap)
    print(root)

main()
