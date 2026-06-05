from unittest.mock import patch

from src.api import _build_query, fetch_articles

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

@patch('src.api.NEWS_API_KEY', 'test_api_key')
@patch('src.api.requests.get')
def test_fetch_articles(mock_get):
    mock_response = mock_get.return_value

    mock_response.json.return_value = {
        'status': 'ok',
        'articles': [
            {
                'title': 'Python news',
                'url': 'https://example.com',
            }
        ],
    }

    result = fetch_articles(
        '2026-06-04',
        ['python'],
        [],
    )

    assert result == [
        {
            'title': 'Python news',
            'url': 'https://example.com',
        }
    ]

    mock_response.raise_for_status.assert_called_once()

    mock_get.assert_called_once_with(
        'https://newsapi.org/v2/everything',
        params={
            'apiKey': 'test_api_key',
            'q': 'python',
            'from': '2026-06-04',
            'to': '2026-06-04',
        },
        timeout=10
    )