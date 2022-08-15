from challenges.compare_versions import compare_version


def test_compare():
    assert compare_version('0.1', '0.2') == -1
    assert compare_version('0.2', '0.1') == 1
    assert compare_version('4.2', '4.2') == 0
    assert compare_version('0.2', '0.12') == -1
    assert compare_version('3.2', '4.12') == -1
    assert compare_version
