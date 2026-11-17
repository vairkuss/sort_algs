from random import sample
from typing import Optional
from algs import *


class Context:

    def __init__(self) -> None:
        self.__alg: Optional[Sort] = None

    def set_alg(self, alg: Sort):
        self.__alg = alg

    def probe(self) -> None:
        if self.__alg is None:
            raise ValueError("ERROR: sorting algorythm isn't set!")
        print(f"TESTING {type(self.__alg).__name__}:")
        rand_arr: list[int] = sample(range(100), 9)
        print(f"> before: {rand_arr}")
        self.__alg.sort(rand_arr)
        print(f"> sorted: {rand_arr}\n")


if __name__ == '__main__':
    ctx: Context = Context()

    ctx.set_alg(BubbleSort())
    ctx.probe()

    ctx.set_alg(SelectionSort())
    ctx.probe()

    ctx.set_alg(InsertionSort())
    ctx.probe()

    ctx.set_alg(MergeSort())
    ctx.probe()

    ctx.set_alg(QuickSort())
    ctx.probe()
