import pytest


@pytest.mark.parametrize("a, b, c", [[1, 2, 3], [1, 2, 4]])
def test_demo(a, b, c):
    """
    pytest.ini 中 send_when=on_fail, 因此预期会有报告发出.
    """
    assert a + b == c
