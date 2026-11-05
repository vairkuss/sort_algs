from random import sample
from typing import Callable
from algs import *
from algs.insertion_sort import insertion_sort


def probe(func: Callable[[list[int]], None]) -> None:
    print(f"TESTING {func.__name__}:")
    rand_arr: list[int] = sample(range(100), 9)
    print(f"> before: {rand_arr}")
    func(rand_arr)
    print(f"> sorted: {rand_arr}\n")


if __name__ == '__main__':
    probe(bubble_sort)
    probe(selection_sort)
    probe(insertion_sort)
    probe(merge_sort)
    probe(quick_sort)
