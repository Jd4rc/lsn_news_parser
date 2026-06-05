from datetime import date


def get_today_date() -> str:
    """Возвращает текущую дату в формате YYYY-MM-DD."""
    return date.today().isoformat()


def normalize_articles(
    articles: list[dict],
) -> list[dict]:
    result = []

    for article in articles:
        result.append({
            'author': article.get('author'),
            'description': article.get('description'),
            'title': article.get('title'),
            'url': article.get('url'),
        })

    return result

