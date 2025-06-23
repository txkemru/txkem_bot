import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("Не установлен BOT_TOKEN в переменных окружения")

# ID администратора (замените на ваш Telegram ID)
ADMIN_ID = int(os.getenv('ADMIN_ID', '123456789')) 