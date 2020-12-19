from helper import Helper
import sys

class MinHeap():

    def __init__(self):
        self.heap = []

    def insert(self, val: int) -> None:
        self.heap.append(val)
        self._heapify()

    def search(self, val: int) -> bool:
        return

    def delete(self, val: int) -> None:
        delete_idx = 0
        for i in range(len(self.heap)):
            if self.heap[i] == val:
                delete_idx = i

        last = self.heap.pop()
        self.heap[delete_idx] = last
        

    def __str__(self) -> None:
        print(self.heap)

    def _heapify(self) -> None:
        """Sorts a number in the heap to maintain heap properties."""
        n_idx = len(self.heap) - 1
        parent_idx = abs(n_idx - 1) // 2
        while self.heap[parent_idx] > self.heap[n_idx]:
            if parent_idx < 0:
                return
            self.heap[parent_idx], self.heap[n_idx] = self.heap[n_idx], self.heap[parent_idx]
            n_idx = parent_idx
            parent_idx = (n_idx - 1) // 2
            

def main():

    low = 0
    high = 5
    length = 40
    
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

main()

