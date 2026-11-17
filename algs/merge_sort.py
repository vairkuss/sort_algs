from . import Sort


class MergeSort(Sort):

    def sort(self, arr: list[int]) -> None:
        arr[:] = self.__break(arr)

    def __break(self, arr: list[int]) -> list[int]:
        """
        breaks provided list and contests it back recursively
        using MergeSort.__contest() method
        :param arr: a part of provided list
        :return: contested part of provided list
        """
        if len(arr) < 2:
             return arr
        mid = len(arr) // 2
        left: list[int] = self.__break(arr[:mid])
        right: list[int] = self.__break(arr[mid:])
        return self.__contest(left, right)

    def __contest(self, left: list[int], right: list[int]) -> list[int]:
        """
        contests left and right halves of the provided
        list's part and merges them
        :param left: left half
        :param right: right half
        :return: merged part of the part of the provided list
        """
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

