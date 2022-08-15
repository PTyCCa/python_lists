import lessons.duplicate


def test_duplicate():
    original = [1, 2, 3]
    ref = original[:]  # a shallow copy

    expected = original * 2
    result = lessons.duplicate.duplicate(ref)
    assert result is None  # function shouldn't return anything
    assert ref == expected
