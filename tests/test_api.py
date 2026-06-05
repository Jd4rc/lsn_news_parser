from src.api import _build_query

def test_build_query_with_include_keywords():
    result = _build_query(
        ['python'],
        []
    )

    assert result == 'python'

def test_build_query_with_exclude_keywords():
    result = _build_query(
        ['python'],
        ['ai']
    )

    assert result == 'python -ai'


def test_build_query_with_only_exclude_keywords():
    result = _build_query(
        [],
    ['ai']
    )
    assert result == '-ai'