import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def save_articles(
        articles: list[dict],
        filename:str
) -> None:
    pass