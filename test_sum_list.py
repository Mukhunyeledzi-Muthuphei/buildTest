import pytest
from sum_list import sum_list

def test_sum_list_with_numbers():
    assert sum_list([1, 2, 3, 4]) == 1
    assert sum_list([0, 0, 0]) == 0
    assert sum_list([-1, 1, -2, 2]) == 0