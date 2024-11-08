import pytest
from main_2 import sort_list  # import the function to be tested


def test_sort_list_ascending():
   assert sort_list([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]


def test_sort_list_descending():
   assert sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_sort_list_mixed():
   assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]


