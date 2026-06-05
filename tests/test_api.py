from src.api import _build_query

def test_build_query_with_include_keywords():
    result = _build_query(
        ['python'],
        []
    )

    assert result == 'python'