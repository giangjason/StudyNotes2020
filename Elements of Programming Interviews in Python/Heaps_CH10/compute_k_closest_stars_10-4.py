# Consider a coordinate system for the Milky Way, in which Earth is at (0,0,0). Model stars as points, and assue distances are in light years.
# The Milky Way consists of approx. 10^12 stars. 
# Design an algorithm that accepts a list of star coordinates and returns the k closest stars to earth.

from __future__ import annotations
from typing import List
import random
import heapq

class Star():

    def __init__(self, name: str, a: int, b: int, c: int) -> Star:
        self.name = name
        self.a = a
        self.b = b
        self.c = c

    def distance(self):
        return self.a ** 2 + self.b ** 2 + self.c ** 2

    
def generate_random_star_list(length: int) -> List[Star]:
    stars = []
    star_map = {}
    for _ in range(length):
        random_star_num = random.randint(1, 9999)
        star_name = "Star_{}".format(str(random_star_num))
        while star_name in star_map:
            random_star_num = random.randint(1, 9999)
            star_name = "Star_{}".format(str(random_star_num))
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        star = Star(star_name, a, b, c)
        stars.append(star)
        star_map[star_name] = star
    return stars

def compute_k_closest_stars(stars: List[Star], k: int) -> List[Star]:
    heap = []
    for star in stars:
        if len(heap) < k:
            heapq.heappush(heap, (-1 * star.distance(), star))
        else:
            heapq.heappushpop(heap, (-1 * star.distance(), star))

    output = []
    while heap:
        star = heapq.heappop(heap)
        output.append(star[1])

    return output

def main():
    length = 15
    stars = generate_random_star_list(length)

    sorted_stars = sorted(stars, key=lambda x: x.distance())
    print([(star.name, star.distance()) for star in sorted_stars])

    k = 5
    k_closest_stars = compute_k_closest_stars(stars, k)
    k_closest_stars.reverse()

    for star in k_closest_stars:
        print("Star Name: {0}. Distance: {1}".format(star.name, star.distance()))
main()
