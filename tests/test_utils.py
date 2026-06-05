from src.utils import normalize_articles, get_today_date
from unittest.mock import patch
from datetime import date

def test_normalize_articles():
    articles = [
        {
            'author': 'John',
            'description': 'Python news',
            'title': 'Python 3.14',
            'url': 'https://example.com',
            'content': 'extra field',
            'source': {'name': 'BBC'},
        }
    ]

    result = normalize_articles(articles)

    assert result == [
        {
            'author': 'John',
            'description': 'Python news',
            'title': 'Python 3.14',
            'url': 'https://example.com',
        }
    ]


def test_normalize_articles_with_missing_fields():
    articles = [
        {
            'author': 'John',
        }
    ]

    result = normalize_articles(articles)

    assert result == [
        {
            'author': 'John',
            'description': None,
            'title': None,
            'url': None,
        }
    ]

@patch('src.utils.date')
def test_get_today_date(mock_date):
    mock_date.today.return_value = date(2026, 6, 4)

    result = get_today_date()

    assert result == '2026-06-04'
