import requests
from src.config import NEWS_API_KEY, logger


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
    if NEWS_API_KEY is None:
        raise ValueError('NEWS_API_KEY not set')


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

    logger.info(
        f'Fetching articles for query: {query}'
    )
    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        logger.info(
            f'Fetched {len(data.get("articles", []))} articles'
        )
    except requests.exceptions.RequestException as err:
        logger.error(
            f'NewsAPI request failed: {err}'
        )
        raise
    return data.get('articles', [])

