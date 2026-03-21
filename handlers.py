# Обработчики команд и сообщений
from telegram import Update
from telegram.ext import ContextTypes
from config import *
from keyboards import *

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user = update.effective_user
    welcome_text = f"""
👋 Добро пожаловать в {RESTAURANT_NAME}!

Я ваш помощник по всем вопросам ресторана. 

Выберите интересующий вас раздел:
    """
    await update.message.reply_text(welcome_text, reply_markup=get_main_keyboard())

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Справка по доступным командам"""
    help_text = """
<b>📚 Доступные команды:</b>

/start - Главное меню
/help - Эта справка
/menu - Открыть меню
/contacts - Контакты
/hours - Часы работы
/offers - Спецпредложения

<b>Также используйте кнопки ниже для навигации.</b>
    """
    await update.message.reply_text(help_text, reply_markup=get_main_keyboard(), parse_mode='HTML')

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать меню"""
    menu_text = """
<b>🍽️ Выберите категорию меню:</b>
    """
    await update.message.reply_text(menu_text, reply_markup=get_menu_keyboard(), parse_mode='HTML')

async def show_menu_category(update: Update, context: ContextTypes.DEFAULT_TYPE, category_key: str, category_name: str):
    """Показать категорию меню"""
    category = MENU.get(category_key, {})
    menu_text = f"<b>{category_name} 📜</b>\n\n"
    
    for dish, price in category.items():
        menu_text += f"• <b>{dish}</b>\n  {price}\n\n"
    
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(menu_text, reply_markup=get_menu_keyboard(), parse_mode='HTML')

async def show_contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать контакты"""
    contacts_text = f"""
<b>📞 Контакты {RESTAURANT_NAME}</b>

<b>📍 Адрес:</b>
{RESTAURANT_ADDRESS}

<b>☎️ Телефон:</b>
{RESTAURANT_PHONE}

<b>📧 Email:</b>
{RESTAURANT_EMAIL}

<b>🌐 Сайт:</b>
{RESTAURANT_WEBSITE}
    """
    await update.message.reply_text(contacts_text, reply_markup=get_contacts_keyboard(), parse_mode='HTML')

async def show_working_hours(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать часы работы"""
    hours_text = "<b>⏰ Часы работы</b>\n\n"
    for day, hours in WORKING_HOURS.items():
        hours_text += f"<b>{day}</b>: {hours}\n"
    
    await update.message.reply_text(hours_text, reply_markup=get_main_keyboard(), parse_mode='HTML')

async def show_special_offers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать спецпредложения"""
    await update.message.reply_text(SPECIAL_OFFERS, reply_markup=get_main_keyboard(), parse_mode='HTML')

async def show_about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """О ресторане"""
    about_text = f"""
<b>ℹ️ О нас</b>

<b>{RESTAURANT_NAME}</b> - это место, где...

🌟 <b>Что нас отличает:</b>
• Авторская кухня от опытного шефа
• Свежие продукты ежедневно
• Уютная атмосфера
• Отличное обслуживание
• Банкеты и корпоративные мероприятия

📍 На протяжении 15 лет мы радуем гостей высочайшим качеством блюд и услуг!

Спасибо, что вы выбираете нас! ❤️
    """
    await update.message.reply_text(about_text, reply_markup=get_main_keyboard(), parse_mode='HTML')

async def handle_booking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Начать процесс бронирования"""
    booking_text = """
<b>🎟️ Бронирование столика</b>

Опишите, пожалуйста, свои пожелания:
• Дата и время
• Количество человек
• Специальные пожелания (если есть)

Наш менеджер свяжется с вами в ближайшее время.
    """
    await update.message.reply_text(booking_text, reply_markup=get_main_keyboard(), parse_mode='HTML')
    context.user_data['waiting_for_booking'] = True

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик текстовых сообщений"""
    text = update.message.text
    
    # Проверка основных кнопок
    if text == "📋 Меню":
        await menu_command(update, context)
    elif text == "📍 Контакты":
        await show_contacts(update, context)
    elif text == "⏰ Часы работы":
        await show_working_hours(update, context)
    elif text == "🎉 Спецпредложения":
        await show_special_offers(update, context)
    elif text == "❓ О нас":
        await show_about(update, context)
    elif text == "📞 Забронировать":
        booking_text = """
<b>🎟️ Бронирование столика</b>

Выберите удобный для вас вариант:
        """
        await update.message.reply_text(booking_text, reply_markup=get_booking_start_keyboard(), parse_mode='HTML')
    elif context.user_data.get('waiting_for_booking'):
        # Если ждем данные для бронирования
        booking_message = f"""
✅ <b>Спасибо за информацию!</b>

Ваше сообщение:
<code>{text}</code>

Наш менеджер свяжется с вами по телефону {RESTAURANT_PHONE} в ближайшее время!

Спасибо, что выбираете нас! 🙏
        """
        await update.message.reply_text(booking_message, reply_markup=get_main_keyboard(), parse_mode='HTML')
        context.user_data['waiting_for_booking'] = False
    else:
        await update.message.reply_text(
            "Пожалуйста, используйте кнопки меню для навигации или введите команду /help",
            reply_markup=get_main_keyboard()
        )

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик callback кнопок"""
    query = update.callback_query
    
    if query.data == "menu_appetizers":
        await show_menu_category(update, context, "Закуски", "🥘 Закуски")
    elif query.data == "menu_mains":
        await show_menu_category(update, context, "Основные блюда", "🍽️ Основные блюда")
    elif query.data == "menu_desserts":
        await show_menu_category(update, context, "Десерты", "🍰 Десерты")
    elif query.data == "menu_drinks":
        await show_menu_category(update, context, "Напитки", "🥤 Напитки")
    elif query.data == "back_to_main":
        welcome_text = f"👋 {RESTAURANT_NAME}\n\nВыберите интересующий вас раздел:"
        await query.answer()
        await query.edit_message_text(welcome_text, reply_markup=get_main_keyboard(), parse_mode='HTML')
    elif query.data == "booking_start":
        query.answer()
        await query.edit_message_text(
            "📝 Пожалуйста, опишите свои пожелания к бронированию (дата, время, количество человек):",
            reply_markup=get_back_button()
        )
        context.user_data['waiting_for_booking'] = True
