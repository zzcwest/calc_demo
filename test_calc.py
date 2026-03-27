import pytest
from calc import my_div


def test_my_div_by_zero():
    my_div(1, 0)
