from challenges.hamming_weight import hamming_weight


def test_hamming():
    assert hamming_weight(0) == 0
    assert hamming_weight(1) == 1
    assert hamming_weight(5) == 2
    assert hamming_weight(10) == 2
    assert hamming_weight(101) == 4
    assert hamming_weight(12345) == 6
