from . import Sort


class QuickSort(Sort):

    def sort(self, arr: list[int]) -> None:
        arr[:] = self.__recursion(arr)

    def __recursion(self, arr: list[int]) -> list[int]:
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
        left: list[int] = self.__recursion(arr[:j+1])
        right: list[int] = self.__recursion(arr[i:-1])
        return left + [pivot] + right
