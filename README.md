# YouTube Analytics CLI

CLI-инструмент для анализа метрик YouTube-видео из CSV-файлов.

## Запуск

```bash
python main.py --files stats1.csv stats2.csv --report clickbait
```

## Доступные отчёты

- `clickbait` — видео с высоким CTR (>15%) и низким удержанием (<40%), отсортированные по убыванию CTR

## Тесты

```bash
pytest
# или с покрытием:
pytest --cov=reports
```

## Зависимости

```bash
pip install -r requirements.txt
```

## Добавление нового отчёта

1. Создай файл в `reports/`, например `reports/my_report.py`
2. Унаследуй класс от `BaseReport` и реализуй метод `generate(data: List[Video]) -> List[Video]`
3. Зарегистрируй в `reports/__init__.py` в словаре `REPORTS`

```python
# reports/__init__.py
from reports.my_report import MyReport

REPORTS = {
    "clickbait": ClickbaitReport,
    "my_report": MyReport,
}
```