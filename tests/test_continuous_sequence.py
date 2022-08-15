from challenges.continuous_sequence import is_continuous_sequence


def test_is_continuous_sequence():
    assert not is_continuous_sequence([])
    assert not is_continuous_sequence([7])
    assert not is_continuous_sequence([5, 3, 2, 8])
    assert not is_continuous_sequence([10, 11, 12, 14, 15])
    assert not is_continuous_sequence([10, 11, 11, 12])
    assert not is_continuous_sequence([5, 6, 6, 8])
    assert is_continuous_sequence([0, 1, 2, 3])
    assert is_continuous_sequence([-5, -4, -3])
    assert is_continuous_sequence([10, 11, 12, 13])
