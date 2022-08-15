from lessons.creation import get_range, get_square_roots


def test_get_square_roots():
    assert get_square_roots(-1) == []
    assert get_square_roots(0) == [0]
    assert get_square_roots(25) == [-5.0, 5.0]


def test_get_range():
    assert get_range(-5) == []
    assert get_range(0) == []
    assert get_range(5) == [0, 1, 2, 3, 4]
