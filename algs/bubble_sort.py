from . import Sort


class BubbleSort(Sort):

    def sort(self, arr: list[int]) -> None:
        swapped: bool = True
        i: int = 0
        while swapped:
            swapped = False
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            i += 1
