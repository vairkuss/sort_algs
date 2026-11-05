def quick_sort(arr: list[int]) -> None:
    arr[:] = quick_sort_recursion(arr)

def quick_sort_recursion(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    i = 0
    while i < len(arr) and arr[i] < arr[-1]:
        i += 1
    j: int = -2
    while not -j > len(arr[i:]) and arr[j] > arr[-1]:
        j -= 1
    print(f"{j=}, {i=}")
    left: list[int] = quick_sort_recursion(arr[:j])
    right: list[int] = quick_sort_recursion(arr[i:])
    return left + [arr[-1]] + right
