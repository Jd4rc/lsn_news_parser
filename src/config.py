from dotenv import load_dotenv
from pathlib import Path
import os
import logging

BASE_DIR = Path(__file__).resolve().parent.parent

LOGS_DIR = BASE_DIR / 'logs'
LOGS_DIR.mkdir(exist_ok=True)

load_dotenv(BASE_DIR / '.env')

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


logging.basicConfig(
    filename=LOGS_DIR / 'news_parser.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)