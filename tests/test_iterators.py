from lessons.iterators import find_second_index


def test_find_second_index():
    assert find_second_index('!', '') is None
    assert find_second_index('!', '!') is None
    assert find_second_index('n', 'clone') is None
    assert find_second_index('n', 'banana') == 4
    assert find_second_index('n', 'cannon') == 3
