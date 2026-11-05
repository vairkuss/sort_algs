from typing import Optional


def merge_sort(arr: list[int]) -> None:
    arr[:] = merge_sort_break(arr)


def merge_sort_break(arr: list[int]) -> list[int]:
    if len(arr) < 2:
         return arr
    mid = len(arr) // 2
    left: list[int] = merge_sort_break(arr[:mid])
    right: list[int] = merge_sort_break(arr[mid:])
    return merge_sort_contest(left, right)


def merge_sort_contest(left: list[int], right: list[int]) -> list[int]:
    if not right:
        return left
    i = j = 0
    merged: list[int] = []
    while i < len(left) or j < len(right):
        if i >= len(left) or j < len(right) and right[j] < left[i]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
    return merged

