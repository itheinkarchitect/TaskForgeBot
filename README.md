# TaskForge

Telegram-бот для управления задачами, созданный на Python с использованием aiogram 3.

## Description

TaskForge — это Telegram-бот, который позволяет пользователям создавать и управлять своими задачами.

В версии MVP бот использует SQLite для хранения данных, благодаря чему задачи сохраняются после перезапуска и разделяются между пользователями.

## Technologies

* Python
* aiogram 3
* SQLite
* Telegram Bot API

## Features

### Task Management

* Добавление задач
* Просмотр списка задач
* Удаление задач
* Завершение задач

### Database

* Хранение задач в SQLite
* Связь задач с пользователями через Telegram ID
* Сохранение данных между запусками

## Commands

```
/start — запуск бота

/task — показать задачи

/add — добавить задачу

/delete — удалить задачу

/complete — завершить задачу

/help — список команд
```

## Project Structure

```
TaskForge/
│
├── bot.py
├── handlers.py
├── database.py
├── keyboards.py
├── config.py
├── requirements.txt
├── README.md
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your own config.py:

```python
TOKEN = "YOUR_BOT_TOKEN"
```

Run:

```bash
python bot.py
```

## Future Improvements

* Улучшение архитектуры проекта
* PostgreSQL вместо SQLite
* Добавление категорий задач
* Добавление дедлайнов
* Добавление уведомлений

## Author

Shoxrux Togayev
