from helper import Helper
import sys

class MinHeap():

    def __init__(self):
        self.heap = []

    def insert(self, val: int) -> None:
        """Inserts an element into the heap and sorts itself to maintain min-heap properties.

        Time complexity:
            Average: O(logn)
            Worst: O(logn)

        Args:
            val (int): The value to insert.
        """
        # Add to the end of the heap
        self.heap.append(val)

        # Determine the index positions of the current element and its parent
        curr_idx = len(self.heap) - 1
        parent_idx = (curr_idx - 1) // 2

        # Repeatedly swap the current element with its parent if the parent is greater.
        while parent_idx >= 0 and self.heap[parent_idx] > self.heap[curr_idx]:
            self.heap[parent_idx], self.heap[curr_idx] = self.heap[curr_idx], self.heap[parent_idx]
            curr_idx = parent_idx
            parent_idx = (curr_idx - 1) // 2

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

    def delete(self, val: int) -> None:
        """Deletes an item from the heap

        Time complexity:
            Average: O(logn)
            Worst: O(logn)

        Args:
            val (int): The value to delete.
        """
        # Find the index of the item to delete
        try:
            curr_idx = self.heap.index(val)
        except:
            # Return out of value is not in heap
            return
        
        # Replace item to delete with last item in heap
        self.heap[curr_idx] = self.heap[-1]

        # Remove last item in the heap
        self.heap.pop()

        self._heapify(curr_idx)

    def get_min(self) -> int:
        """Gets the min element in the heap.

        Time complexity:
            Retrieval: O(1)
            Heapify: O(logn)

        Returns:
            int: The min element.
        """
        # Get the top item in the heap
        min_val = self.heap[0]

        # Replace top item in the heap with last item
        self.heap[0] = self.heap[-1]

        # Remove the last item in the heap
        self.heap.pop()

        self._heapify()

        return min_val
            
    def _heapify(self, curr_idx: int = 0) -> None:
        # Heapify the heap
        left_idx = 2 * curr_idx + 1
        right_idx = 2 * curr_idx + 2

        # Return out of there are no left or right child
        if left_idx > len(self.heap)-1 or right_idx > len(self.heap)-1:
            return

        while self.heap[left_idx] < self.heap[curr_idx] or self.heap[right_idx] < self.heap[curr_idx]:
            # If both the left and right child are smaller than the parent, swap with the smaller child
            if self.heap[left_idx] < self.heap[curr_idx] and self.heap[right_idx] < self.heap[curr_idx]:
                if self.heap[left_idx] < self.heap[right_idx]:
                    self.heap[left_idx], self.heap[curr_idx] = self.heap[curr_idx], self.heap[left_idx]
                    curr_idx = left_idx
                else:
                    self.heap[right_idx], self.heap[curr_idx] = self.heap[curr_idx], self.heap[right_idx]
                    curr_idx = right_idx
            # Swap with the left if the left is smaller
            elif self.heap[left_idx] < self.heap[curr_idx]:
                self.heap[left_idx], self.heap[curr_idx] = self.heap[curr_idx], self.heap[left_idx]
                curr_idx = left_idx
            # Swap with the right if the right is smaller
            else:
                self.heap[right_idx], self.heap[curr_idx] = self.heap[curr_idx], self.heap[right_idx]
                curr_idx = right_idx
            left_idx = 2 * curr_idx + 1
            right_idx = 2 * curr_idx + 2

            # If the left or right child have indexes greater than the length of the heap,
            # that means we have reached the end of the heap. Break out of the loop.
            if left_idx > len(self.heap)-1 or right_idx > len(self.heap)-1:
                break

def main():

    low = 0
    high = 100
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
    print("-----Min Heap-----")
    heap = MinHeap()
    for num in nums:
        heap.insert(num)
    print(heap.heap)
    root = helper.construct_binary_tree(heap.heap)
    print(root)

    print("\n")
    print("-----Retrieving Min-----")
    min_val = heap.get_min()
    print("Min item:", min_val)
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

