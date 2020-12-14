from typing import List
import random

class Helper():

    def generate_random_list(self, low: int, high: int, length: int) -> List[int]:
        """Generates a random list of numbers

        Args:
            low (int): The lowest possible value in the list
            high (int): The highest possible value in the list
            length (int): The length of the list

        Returns:
            List[int]: Returns a random list of numbers
        """
        return [random.randint(low, high) for _ in range(length)]

    