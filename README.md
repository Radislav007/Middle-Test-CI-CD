# 🧠 Middle-Test-CI-CD

Скрипт на Python, який читає `.txt` файл, знаходить **10 найпопулярніших слів** і записує їх у новий файл у форматі:


## 🚀 Функціонал

- Підрахунок найчастіших слів
- Юніт-тести з `pytest` + `fixtures` та `parametrize`
- Автоматичний CI (GitHub Actions)
- Перевірка на PEP8 (`flake8`)
- Генерація звіту у форматі `pytest-html`

## 📂 Запуск

### Встановлення залежностей:

```bash
pip install -r requirements.txt
python main.py
pytest
pytest --html=report.html
