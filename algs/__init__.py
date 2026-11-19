from .sort import Sort
from .bubble_sort import BubbleSort
from .selection_sort import SelectionSort
from .insertion_sort import InsertionSort
from .merge_sort import MergeSort
from .quick_sort import QuickSort

algs = {
    "bubble_sort": BubbleSort(),
    "selection_sort": SelectionSort(),
    "insertion_sort": InsertionSort(),
    "merge_sort": MergeSort(),
    "quick_sort": QuickSort()
}
