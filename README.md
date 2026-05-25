# 🤖 Telegram Bot (Python)

Простой Telegram-бот на Python с использованием [aiogram v3](https://docs.aiogram.dev/en/latest/).

## 📦 Стек

| Библиотека | Версия | Назначение |
|---|---|---|
| [aiogram](https://github.com/aiogram/aiogram) | 3.7.0 | Асинхронный фреймворк для Telegram Bot API |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | 1.0.1 | Загрузка переменных окружения из `.env` |

## 🚀 Быстрый старт

### 1. Клонируй репозиторий
```bash
git clone https://github.com/d08163484-lab/telegram-bot-python.git
cd telegram-bot-python
```

### 2. Создай виртуальное окружение и установи зависимости
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Настрой переменные окружения
```bash
cp .env.example .env
# Открой .env и вставь токен своего бота (получи у @BotFather)
```

### 4. Запусти бота
```bash
python bot.py
```

## 📁 Структура проекта

```
telegram-bot-python/
├── bot.py            # Точка входа, хендлеры команд
├── requirements.txt  # Зависимости проекта
├── .env.example      # Шаблон переменных окружения
├── .gitignore        # Исключения для Git
└── README.md         # Документация
```

## 🛠️ Команды бота

| Команда | Описание |
|---|---|
| `/start` | Приветственное сообщение |
| `/help` | Список доступных команд |
| `/echo` | Бот повторяет следующее сообщение |

## 📝 Как получить токен

1. Открой [@BotFather](https://t.me/BotFather) в Telegram
2. Напиши `/newbot`
3. Следуй инструкциям и скопируй полученный токен в `.env`

## 📄 Лицензия

MIT — делай что хочешь.
