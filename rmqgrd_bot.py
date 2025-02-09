from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Токен вашего бота (замените на ваш токен)
TOKEN = "7015032914:AAGcFW6vVP_yArlmwPpAAE7h7iZcrswrAIM"

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я твой первый бот. Как дела?")

# Функция для обработки текстовых сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    await update.message.reply_text(f"Вы сказали: {user_text}")

# Основная функция
def main():
    # Создаем объект Application и передаем ему токен
    application = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Устанавливаем вебхук и запускаем сервер
    application.run_webhook(
        listen="0.0.0.0",  # Слушаем все интерфейсы
        port=10000,        # Порт, который будет слушать бот
        webhook_url="https://rmqgrd-bot.onrender.com",  # URL вашего бота
        cert=None          # Не используем сертификат
    )

if __name__ == "__main__":
    main()
