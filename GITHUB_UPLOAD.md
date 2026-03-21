# 🚀 Инструкция по загрузке на GitHub

## Шаг 1: Инициализация локального Git репозитория

Откройте PowerShell в папке проекта и выполните:

```powershell
git init
git config user.name "Ваше имя"
git config user.email "ваш.email@example.com"
```

## Шаг 2: Добавьте файлы в Git

```powershell
git add .
git status  # для проверки добавленных файлов
```

## Шаг 3: Создайте первый коммит

```powershell
git commit -m "Initial commit: Telegram restaurant bot"
```

## Шаг 4: Создайте репозиторий на GitHub

1. Перейдите на [github.com](https://github.com)
2. Нажмите кнопку `+` в правом верхнем углу
3. Выберите "New repository"
4. Дайте имя репозиторию: `telegram_restaurant_bot`
5. Добавьте описание
6. Нажмите "Create repository"

## Шаг 5: Подключите GitHub репозиторий

Скопируйте эту команду в PowerShell (замените USERNAME на ваше имя пользователя):

```powershell
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/telegram_restaurant_bot.git
git push -u origin main
```

## Шаг 6: Проверьте результат

- Откройте ваш репозиторий: https://github.com/YOUR_USERNAME/telegram_restaurant_bot
- Вы должны увидеть все файлы проекта

## Дальнейшие обновления

Для загрузки изменений:

```powershell
git add .
git commit -m "Описание изменений"
git push
```

## ✅ Что загружено на GitHub

- 📄 main.py - основной файл бота
- 📄 config.py - конфигурация ресторана
- 📄 handlers.py - обработчики команд
- 📄 keyboards.py - клавиатуры
- 📄 requirements.txt - зависимости
- 📄 README.md - документация
- 📄 LICENSE - лицензия MIT
- 📄 .gitignore - исключения для Git
- 📄 .env.example - пример переменных окружения

## 🔐 ВАЖНО: .env файл

**НИКОГДА не загружайте файл `.env` на GitHub!**

Используйте `.env.example` для примера конфигурации.

## 📝 Советы по GitHub

- Писать понятные описания коммитов
- Часто делать коммиты (не один большой)
- Использовать русский или английский язык в коммитах
- Добавлять описания в README для новых функций

---

Готово! Ваш бот теперь на GitHub! 🎉
