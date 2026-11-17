from . import Sort


class SelectionSort(Sort):

    def sort(self, arr: list[int]) -> None:
        for i in range(len(arr)):
            lowest: int = i
            for j in range(i + 1, len(arr)):
                if arr[lowest] > arr[j]:
                    lowest = j
            arr[i], arr[lowest] = arr[lowest], arr[i]
