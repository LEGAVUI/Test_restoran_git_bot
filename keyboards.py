# Клавиатуры для бота
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    """Основная клавиатура с главными кнопками"""
    button_list = [
        [KeyboardButton("📋 Меню")],
        [KeyboardButton("📍 Контакты"), KeyboardButton("⏰ Часы работы")],
        [KeyboardButton("🎉 Спецпредложения"), KeyboardButton("📞 Забронировать")],
        [KeyboardButton("❓ О нас")]
    ]
    return ReplyKeyboardMarkup(button_list, resize_keyboard=True)

def get_menu_keyboard():
    """Клавиатура для навигации по меню"""
    buttons = [
        [InlineKeyboardButton("🥘 Закуски", callback_data="menu_appetizers")],
        [InlineKeyboardButton("🍽️ Основные блюда", callback_data="menu_mains")],
        [InlineKeyboardButton("🍰 Десерты", callback_data="menu_desserts")],
        [InlineKeyboardButton("🥤 Напитки", callback_data="menu_drinks")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(buttons)

def get_contacts_keyboard():
    """Клавиатура с контактами"""
    buttons = [
        [InlineKeyboardButton("📞 Позвонить", callback_data="call")],
        [InlineKeyboardButton("📧 Email", callback_data="email")],
        [InlineKeyboardButton("🌐 Сайт", url="https://restoran.ru")],
        [InlineKeyboardButton("📍 Карта", callback_data="location")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(buttons)

def get_back_button():
    """Кнопка для возврата"""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")]
    ])

def get_booking_start_keyboard():
    """Клавиатура для начала бронирования"""
    buttons = [
        [InlineKeyboardButton("✅ Забронировать столик", callback_data="booking_start")],
        [InlineKeyboardButton("❓ Задать вопрос", callback_data="ask_question")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(buttons)
