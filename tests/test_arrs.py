import pytest

from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


@pytest.mark.parametrize('a, b, c, result', [([1, 2, 3], 1, None, [2, 3]),
                                             ([], None, None, []),
                                             ([1, 2, 3, 4], -5, None, [1, 2, 3, 4]),
                                             ([1, 2, 3, 4], -3, None, [2, 3, 4]),
                                             ([1, 2, 3, 4], -3, -4, [])
                                             ]
                         )
def test_slice(a, b, c, result):
    assert arrs.my_slice(a, b, c) == result
