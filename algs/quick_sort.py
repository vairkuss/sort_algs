def quick_sort(arr: list[int]) -> None:
    arr[:] = quick_sort_recursion(arr)

def quick_sort_recursion(arr: list[int], recursion = 0) -> list[int]:
    if len(arr) < 2:
        return arr
    pivot: int = arr[-1] #######
    i: int = 0
    j: int = len(arr) - 2
    while i < len(arr) - 1 and min(arr[i], arr[j]) < pivot:
        at_i: int = arr[i] #######
        at_j: int = arr[j] #######
        swap: bool = at_i > at_j  ####### bp
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
        in_bounds: bool = i < len(arr) - 1 #######
        searching: bool = min(arr[i], arr[j]) < pivot #######
        loop: bool = in_bounds and searching ####### bp
    while j >= i and max(arr[i], arr[j]) > pivot:
        at_i: int = arr[i] #######
        at_j: int = arr[j] #######
        swap: bool = at_i > at_j ####### bp
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        j -= 1
        in_bounds: bool = j >= 0 #######
        searching: bool = max(arr[j], arr[i]) > pivot #######
        loop: bool = in_bounds and searching ####### bp
    l, r = arr[:j], arr[i:-1] ####### bp
    left: list[int] = quick_sort_recursion(arr[:j], recursion + 1)
    right: list[int] = quick_sort_recursion(arr[i:-1], recursion + 1)
    print(f"{recursion}. ", [left, [pivot], right]) #######
    return left + [arr[-1]] + right # bp
