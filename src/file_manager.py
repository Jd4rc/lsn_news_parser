import json
from pathlib import Path
from datetime import datetime
from src.config import logger

BASE_DIR = Path(__file__).resolve().parent.parent



def save_articles(
        articles: list[dict],
        filename:str
) -> None:
    file_path = BASE_DIR / 'data' / filename

    logger.info(
        f'Saving articles to {file_path}'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

    logger.info(
        f'Successfully saved {len(articles)} articles'
    )

def generate_filename(date:str) -> str:
    return (
        f'news_{date}.json'
    )