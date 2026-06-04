from datetime import date


def get_today_date() -> str:
    """Возвращает текущую дату в формате YYYY-MM-DD."""
    return date.today().isoformat()

