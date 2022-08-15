# flake8: noqa

from challenges.chunks import chunked


def test_chunked_list():
    assert chunked(2, ['a', 'b', 'c', 'd']) == [['a', 'b'], ['c', 'd']]
    assert chunked(3, ['e', 'f', 'h', 'i']) == [['e', 'f', 'h'], ['i']]
    assert chunked(4, ['g', 'k', 'l', 'm']) == [['g', 'k', 'l', 'm']]
    assert chunked(4, []) == []
    assert chunked(2, ['n']) == [['n']]
    assert chunked(2, ['a', 'b', 'c', 'd', 'e', 'f']) == [['a', 'b'], ['c', 'd'], ['e', 'f']]


def test_chunked_tuple():
    assert chunked(2, ('A', 'B', 'C', 'D')) == [('A', 'B'), ('C', 'D')]
    assert chunked(3, ('E', 'F', 'H', 'I')) == [('E', 'F', 'H'), ('I',)]
    assert chunked(4, ('G', 'K', 'L', 'M')) == [('G', 'K', 'L', 'M')]
    assert chunked(4, []) == []
    assert chunked(2, ('N',)) == [('N',)]
    assert chunked(2, ('A', 'B', 'C', 'D', 'E', 'F')) == [('A', 'B'), ('C', 'D'), ('E', 'F')]


def test_chunked_str():
    assert chunked(2, 'abcd') == ['ab', 'cd']
    assert chunked(3, 'efhi') == ['efh', 'i']
    assert chunked(4, 'gklm') == ['gklm']
    assert chunked(4, '') == []
    assert chunked(2, 'x') == ['x']
    assert chunked(2, 'abcdef') == ['ab', 'cd', 'ef']
