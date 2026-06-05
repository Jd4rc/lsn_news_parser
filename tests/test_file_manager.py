import json

from src.file_manager import generate_filename
from src.file_manager import save_articles

def test_generate_filename():
    result = generate_filename('2026-06-04')

    assert result == 'news_2026-06-04.json'