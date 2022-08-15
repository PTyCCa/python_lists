from challenges.length_of_last_word import length_of_last_word


def test_length_of_last_word():
    assert length_of_last_word('') == 0
    assert length_of_last_word(' \t\n') == 0
    assert length_of_last_word('hi') == 2
    assert length_of_last_word('  cat') == 3
    assert length_of_last_word('man in black') == 5
    assert length_of_last_word('hello, world!') == 6
    assert length_of_last_word('hello, wOrLd!    ') == 6
    assert length_of_last_word('hello\t\nworld') == 5
