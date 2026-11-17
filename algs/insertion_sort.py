from . import Sort


class InsertionSort(Sort):
    
    def sort(self, arr: list[int]) -> None:
        for i in range(1, len(arr)):
            j: int = i
            while j > 0 and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
