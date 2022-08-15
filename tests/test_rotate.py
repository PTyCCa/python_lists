import lessons.rotate


def test_rotate():
    ref = [1, 2, 3]
    result = lessons.rotate.rotate(ref)
    assert result is None  # Function shouldn't return anything!
    assert ref == [3, 1, 2]


def test_rotate_empty_list():
    ref = []
    lessons.rotate.rotate(ref)
    assert ref == []
