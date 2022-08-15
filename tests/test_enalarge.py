from challenges.enlarge import enlarge


def test_enlarge():
    assert enlarge([]) == []
    assert enlarge(['']) == ['', '']
    assert enlarge([
        'A',
    ]) == [
        'AA',
        'AA',
    ]
    assert enlarge([
        ' *',
        '# ',
    ]) == [
        '  **',
        '  **',
        '##  ',
        '##  ',
    ]
