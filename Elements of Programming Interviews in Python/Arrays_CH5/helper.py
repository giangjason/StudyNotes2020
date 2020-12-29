from typing import List
import random

class Helper:

    def generate_random_list(self, low: int, high: int, length: int) -> List[int]:
        return [random.randint(low, high) for _ in range(length)]