import json
import logging
from src.file_manager import generate_filename
from src.file_manager import save_articles

def test_generate_filename():
    result = generate_filename('2026-06-04')

    assert result == 'news_2026-06-04.json'


def test_save_articles(tmp_path, monkeypatch):
    data_dir = tmp_path / 'data'
    data_dir.mkdir()


    monkeypatch.setattr(
        'src.file_manager.BASE_DIR',
        tmp_path
    )

    articles = [
        {
            'author': 'John',
            'description': 'Python news',
            'title': 'Python 3.14',
            'url': 'https://example.com',
        }
    ]

    save_articles(
        articles,
        'news_2026-06-04.json',
    )

    file_path = data_dir / 'news_2026-06-04.json'

    assert file_path.exists()

    save_article = json.loads(
        file_path.read_text(encoding='utf-8')
    )

    assert save_article == articles

def test_save_articles_logging(tmp_path, monkeypatch, caplog):
    data_dir = tmp_path / 'data'
    data_dir.mkdir()

    monkeypatch.setattr(
        'src.file_manager.BASE_DIR',
        tmp_path
    )

    articles = [
        {
            'author': 'John',
            'description': 'Text',
            'title': 'Python',
            'url': 'https://example.com',
        }
    ]

    with caplog.at_level(logging.INFO):
        save_articles(
            articles,
            'news_2026-06-04.json'
        )
    assert 'Saving articles to' in caplog.text
    assert 'Successfully saved 1 articles' in caplog.text