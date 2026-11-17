from abc import ABC, abstractmethod


class Sort(ABC):

    @abstractmethod
    def sort(self, arr: list[int]) -> None:
        """
        sorts provided list
        :param arr:
        """
        ...