def quick_sort(arr: list[int]) -> None:
    arr[:] = quick_sort_recursion(arr)

def quick_sort_recursion(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    pivot: int = arr[-1]
    i: int = 0
    j: int = len(arr) - 2
    while i <= j:
        if arr[i] < pivot:
            i += 1
        elif arr[j] >= pivot:
            j -= 1
        elif arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    left: list[int] = quick_sort_recursion(arr[:j+1])
    right: list[int] = quick_sort_recursion(arr[i:-1])
    return left + [pivot] + right
