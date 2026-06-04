import requests
from src.config import NEWS_API_KEY


def _build_query(
    include_keywords: list[str],
    exclude_keywords: list[str],
) -> str:
    query = include_keywords.copy()

    for word in exclude_keywords:
        query.append(f'-{word}')

    return ' '.join(query)

def fetch_articles(
    date: str,
    include_keywords: list[str],
    exclude_keywords: list[str],
) -> list[dict]:
    url = 'https://newsapi.org/v2/everything'

    query = _build_query(
        include_keywords,
        exclude_keywords
    )

    params = {
        'apiKey': NEWS_API_KEY,
        'q': query,
        'from': date,
        'to': date,
    }

    response.

    return None

