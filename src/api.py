from dotenv import load_dotenv
import os

load_dotenv('.env')

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def _build_query(
    include_keywords: list[str],
    exclude_keywords: list[str],
) -> str:
    query = include_keywords.copy()

    for word in exclude_keywords:
        query.append(f'-{word}')

    return ' '.join(query)

def fetch_articles(

) -> list[dict]:
    url = 'https://newsapi.org/v2/everything'

    params = {
        'apiKey': NEWS_API_KEY,
        'q':include_keywords
    }

    return None

