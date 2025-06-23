import asyncio
import logging
import signal
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from bot.config import BOT_TOKEN
from bot.handlers import router

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

# Глобальные переменные для graceful shutdown
bot = None
dp = None

async def on_startup():
    """Действия при запуске бота"""
    logging.info("Бот запускается...")
    try:
        # Проверяем подключение к Telegram
        me = await bot.get_me()
        logging.info(f"Бот успешно подключен: @{me.username} (ID: {me.id})")
    except Exception as e:
        logging.error(f"Ошибка при подключении к Telegram: {e}")
        sys.exit(1)

async def on_shutdown():
    """Действия при остановке бота"""
    logging.info("Бот останавливается...")
    if bot:
        await bot.session.close()
    logging.info("Бот остановлен")

def signal_handler(signum, frame):
    """Обработчик сигналов для graceful shutdown"""
    logging.info(f"Получен сигнал {signum}, начинаем graceful shutdown...")
    asyncio.create_task(shutdown())

async def shutdown():
    """Корректное завершение работы"""
    await on_shutdown()
    sys.exit(0)

async def main():
    global bot, dp
    
    # Регистрируем обработчики сигналов
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        # Инициализация бота и диспетчера
        bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        
        # Создаем хранилище состояний
        storage = MemoryStorage()
        dp = Dispatcher(storage=storage)
        
        # Регистрация роутера
        dp.include_router(router)
        
        # Регистрируем обработчики событий
        dp.startup.register(on_startup)
        dp.shutdown.register(on_shutdown)
        
        # Запуск бота
        logging.info("Запускаем polling...")
        await dp.start_polling(bot, polling_timeout=30, close_bot_session=True)
        
    except Exception as e:
        logging.error(f"Критическая ошибка при запуске бота: {e}")
        if bot:
            await bot.session.close()
        sys.exit(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Получен сигнал прерывания")
    except Exception as e:
        logging.error(f"Неожиданная ошибка: {e}")
        sys.exit(1) 