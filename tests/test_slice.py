import lessons.slice


def test_rotated_right():
    source = [1, 2, 3, 4]
    result = lessons.slice.rotated_right(source)
    assert result is not source  # Function should return a new list!
    assert source == [1, 2, 3, 4]  # Function shouldn't change the source list!
    assert result == [4, 1, 2, 3]


def test_rotated_left():
    source = "ABCD"
    result = lessons.slice.rotated_left(source)
    assert result == "BCDA"


def test_symmetricity():
    source = (1, True, "foo")
    result1 = lessons.slice.rotated_right(lessons.slice.rotated_left(source))
    assert result1 == source
    result2 = lessons.slice.rotated_left(lessons.slice.rotated_right(source))
    assert result2 == source
