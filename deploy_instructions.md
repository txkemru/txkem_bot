# Инструкции по деплою на Render

## Шаг 1: Подготовка проекта для Git

```bash
# Инициализируйте Git репозиторий
git init

# Добавьте все файлы
git add .

# Создайте первый коммит
git commit -m "Initial commit: Telegram Personal Manager Bot"
```

## Шаг 2: Создание репозитория на GitHub

1. Зайдите на [github.com](https://github.com)
2. Создайте новый репозиторий (например: `telegram-personal-manager-bot`)
3. **НЕ** добавляйте README, .gitignore или лицензию (они уже есть)
4. Скопируйте URL репозитория

## Шаг 3: Загрузка кода на GitHub

```bash
# Добавьте удалённый репозиторий
git remote add origin https://github.com/YOUR_USERNAME/telegram-personal-manager-bot.git

# Переименуйте ветку в main (если нужно)
git branch -M main

# Загрузите код
git push -u origin main
```

## Шаг 4: Деплой на Render

1. Зайдите на [render.com](https://render.com)
2. Нажмите "New +" → "Web Service"
3. Подключите ваш GitHub репозиторий
4. Render автоматически определит настройки из `render.yaml`

## Шаг 5: Настройка переменных окружения

В настройках Render добавьте переменные окружения:

- **BOT_TOKEN** = ваш_токен_бота_от_botfather
- **ADMIN_ID** = ваш_telegram_id

## Шаг 6: Запуск

Render автоматически:
1. Установит зависимости из `requirements.txt`
2. Запустит бота командой `python -m bot.main`
3. Бот будет работать 24/7

## Проверка работы

1. Найдите вашего бота в Telegram
2. Отправьте `/start`
3. Проверьте все функции

## Обновления

Для обновления бота:
```bash
git add .
git commit -m "Update bot"
git push origin main
```

Render автоматически перезапустит бота с новым кодом.

## Важные файлы

- `.gitignore` - исключает ненужные файлы
- `requirements.txt` - зависимости Python
- `render.yaml` - настройки для Render
- `runtime.txt` - версия Python
- `Procfile` - команда запуска 