"""
Telegram Бот "Визитка" для ресторана

Этот бот позволяет клиентам:
- Просмотреть меню и цены
- Узнать контакты и часы работы
- Ознакомиться со спецпредложениями
- Забронировать столик
- Получить информацию о ресторане
"""

import logging
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)
from handlers import *
from config import BOT_TOKEN

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Запуск бота"""
    # Создание приложения
    application = Application.builder().token(BOT_TOKEN).build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("menu", menu_command))
    application.add_handler(CommandHandler("contacts", show_contacts))
    application.add_handler(CommandHandler("hours", show_working_hours))
    application.add_handler(CommandHandler("offers", show_special_offers))

    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Обработчик callback кнопок
    application.add_handler(CallbackQueryHandler(handle_callback))

    # Запуск бота
    logger.info("Бот запущен!")
    application.run_polling(allowed_updates=['message', 'callback_query'])

if __name__ == '__main__':
    main()
