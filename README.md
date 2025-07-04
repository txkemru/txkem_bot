# Telegram Personal Manager Bot

Персональный менеджер-бот для Telegram с интерактивным меню на инлайн-кнопках и системой заказов.

## Возможности

- 📌 Информация о разработчике с Telegraph
- 💼 Интерактивные услуги с системой заказов
- 📚 Полезные ресурсы по категориям
- ✉️ Контактная информация
- 🔔 Автоматические уведомления о заказах

## Услуги

- 🤖 **Чат-боты** - умные боты с базой данных и логикой
- 🌐 **Веб-приложения** - полноценные веб-сервисы
- 📱 **Telegram Mini App** - встроенные приложения в Telegram
- 🧠 **Интеграция AI** - подключение искусственного интеллекта
- ⚡ **Автоматизация** - скрипты и системы автоматизации

## Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd my_chat_bot
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` на основе `env_example.txt`:
```bash
cp env_example.txt .env
```

4. Отредактируйте файл `.env` и добавьте токен бота и ваш ID:
```
BOT_TOKEN=your_actual_bot_token_here
ADMIN_ID=your_telegram_id_here
```

## Получение токена бота

1. Найдите @BotFather в Telegram
2. Отправьте команду `/newbot`
3. Следуйте инструкциям для создания бота
4. Скопируйте полученный токен в файл `.env`

## Получение вашего Telegram ID

1. Найдите @userinfobot в Telegram
2. Отправьте любое сообщение
3. Бот покажет ваш ID
4. Скопируйте ID в файл `.env` в переменную `ADMIN_ID`

## Запуск локально

```bash
python -m bot.main
```



## Система заказов

### Для пользователей:
1. Выберите "💼 Услуги" в главном меню
2. Выберите интересующую услугу
3. Изучите описание и нажмите "🚀 Начать"
4. Заполните информацию о проекте
5. Получите подтверждение заявки

### Для администратора:
- При каждом новом заказе бот автоматически отправляет уведомление
- Уведомление содержит: имя пользователя, username, ID, выбранную услугу, дату
- Администратор может сразу связаться с клиентом

## Структура проекта

```
bot/
├── main.py      # Основной файл бота
├── handlers.py  # Обработчики команд и callback
├── texts.py     # Тексты для всех разделов
├── states.py    # Состояния для системы заказов
└── config.py    # Конфигурация (токен бота, ID админа)
```

## Технологии

- Python 3.10+
- aiogram 3.x
- asyncio
- python-dotenv

## Использование

1. Запустите бота командой `/start`
2. Используйте инлайн-кнопки для навигации
3. Заказывайте услуги через систему заказов
4. Получайте уведомления о новых заявках (если вы админ)

## Лицензия

MIT 
