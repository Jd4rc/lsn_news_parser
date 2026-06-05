from src.utils import normalize_articles

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