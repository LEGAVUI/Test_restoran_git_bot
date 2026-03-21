# 🍽️ Telegram Бот "Визитка" для ресторана

Полнофункциональный Telegram бот для ресторана, который позволяет клиентам получать информацию о меню, часах работы, контактах и бронировать столик.

## 📋 Возможности

- ✅ **Меню** - просмотр категорий блюд и цен
- ✅ **Контакты** - адрес, телефон, email, сайт
- ✅ **Часы работы** - расписание на разные дни недели
- ✅ **Спецпредложения** - актуальные скидки и предложения
- ✅ **Бронирование** - возможность забронировать столик
- ✅ **О ресторане** - информация об учреждении
- ✅ **Интуитивный интерфейс** - удобные кнопки и inline-кнопки
- ✅ **HTML-форматирование** - красивые сообщения

## 🛠️ Требования

- Python 3.8+
- Telegram Bot Token (от @BotFather)

## ⚙️ Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/YOUR_USERNAME/telegram_restaurant_bot.git
cd telegram_restaurant_bot
```

### 2. Создание виртуального окружения

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

```bash
# Скопируйте пример конфига
copy .env.example .env

# Отредактируйте .env и добавьте ваш BOT_TOKEN
# BOT_TOKEN=YOUR_ACTUAL_TOKEN_HERE
```

## 🚀 Запуск бота

```bash
python main.py
```

Бот начнет слушать обновления от Telegram и будет готов к работе!

## 📂 Структура проекта

```
telegram_restaurant_bot/
│
├── main.py              # Главный файл бота
├── config.py            # Конфигурация и данные ресторана
├── handlers.py          # Обработчики команд и сообщений
├── keyboards.py         # Клавиатуры и inline-кнопки
├── requirements.txt     # Зависимости Python
├── .env.example         # Пример файла окружения
├── .gitignore           # Исключения для Git
└── README.md            # Этот файл
```

## 🎮 Команды бота

| Команда | Описание |
|---------|---------|
| `/start` | Запуск бота, главное меню |
| `/menu` | Открыть меню ресторана |
| `/contacts` | Показать контакты |
| `/hours` | Часы работы |
| `/offers` | Спецпредложения |
| `/help` | Справка по командам |

## 🎨 Кастомизация

### Изменение данных ресторана

Отредактируйте файл `config.py`:

```python
RESTAURANT_NAME = "Ваше название"
RESTAURANT_ADDRESS = "Адрес ресторана"
RESTAURANT_PHONE = "+7 (XXX) XXX-XX-XX"
RESTAURANT_EMAIL = "email@example.com"
RESTAURANT_WEBSITE = "https://yoursite.com"
```

### Изменение меню

В `config.py` отредактируйте словарь `MENU`:

```python
MENU = {
    "Категория": {
        "Блюдо": "Цена",
        "Блюдо 2": "Цена 2"
    }
}
```

### Изменение часов работы

В `config.py` отредактируйте словарь `WORKING_HOURS`:

```python
WORKING_HOURS = {
    "ПН-ЧТ": "11:00 - 23:00",
    "ПТ-СБ": "11:00 - 01:00"
}
```

## 📚 Создание бота в Telegram

1. Откройте Telegram и найдите [@BotFather](https://t.me/BotFather)
2. Отправьте команду `/newbot`
3. Следуйте инструкциям для создания бота
4. Скопируйте полученный token
5. Вставьте token в файл `.env`

## 🚀 Развертывание

### На heroku.com

1. Создайте аккаунт на [Heroku](https://heroku.com)
2. Установите [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. Создайте `Procfile`:
```
worker: python main.py
```
4. Разверните приложение:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### На PythonAnywhere

1. Создайте аккаунт на [PythonAnywhere](https://www.pythonanywhere.com/)
2. Загрузите файлы проекта
3. Создайте веб-приложение с использованием Python
4. Установите зависимости через консоль

## 📝 Лицензия

MIT License - см. файл LICENSE

## 👨‍💻 Автор

Создано для ресторанного бизнеса

## 📞 Поддержка

Если у вас есть вопросы или предложения, создайте Issue в репозитории.

## 🔄 История изменений

### v1.0 (2026-03-21)
- ✨ Первая версия бота
- 🎨 Интуитивный интерфейс
- 📋 Полное меню ресторана
- 📞 Контакты и часы работы
- 🎟️ Функция бронирования

---

**Спасибо за использование нашего бота!** 🙏
