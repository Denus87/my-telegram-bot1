from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

AFFILIATE_LINK = "https://alipartner.com/?ref=12345"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Напиши название товара, например: 'наушники'.")

def handle_message(update: Update, context: CallbackContext):
    user_query = update.message.text
    update.message.reply_text(f"🔍 Товары по запросу '{user_query}':\n{AFFILIATE_LINK}")

def main():
    TOKEN = "7708943630:AAHqxJQACx26l15yTLeKQQLEx55v4ASkXkM"
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()