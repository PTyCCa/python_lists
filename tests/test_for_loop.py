import lessons.for_loop


def test_find_index():
    assert lessons.for_loop.find_index(42, [1, 2, 3]) is None
    assert lessons.for_loop.find_index(2, []) is None
    assert lessons.for_loop.find_index(2, [1, 2, 3]) == 1
    assert lessons.for_loop.find_index("l", "hello") == 2
