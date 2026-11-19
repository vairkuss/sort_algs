from time import process_time
from random import sample
from typing import Optional, Generator
from algs import *


class Context:

    def __init__(self) -> None:
        self.__alg: Optional[Sort] = None

    def set_alg(self, alg: Sort):
        self.__alg = alg

    def get_sort_speed(self, size: int) -> float | int:
        if self.__alg is None:
            raise ValueError("ERROR: sorting algorythm isn't set!")
        rand_arr: list[int] = sample(range(size), size)
        start: float | int = process_time()
        self.__alg.sort(rand_arr)
        end: float | int = process_time()
        return end - start


ctx: Context = Context()

def loop_through_strategies(size: int) -> Generator[tuple[str, float | int], None, None]:
    for alg_name in algs:
        ctx.set_alg(algs[alg_name])
        yield alg_name, ctx.get_sort_speed(size)


if __name__ == '__main__':
    for i in range(2, 6):
        print(f"List size has {i} zeroes: {10 ** i}")
        for name, time in loop_through_strategies(10 ** i):
            print(f"> {name}: {time}")
        print()
