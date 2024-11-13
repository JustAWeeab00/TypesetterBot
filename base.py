from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Replace 'YOUR_TOKEN' with the token you received from BotFather
TOKEN = 'YOUR_TOKEN'

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your bot. Type /help to see what I can do.")

# Help command handler
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("I'm here to assist you! Use /start to restart or just chat with me.")

# Echo handler for text messages
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main():
    # Set up the Updater with your bot token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Register a message handler to echo messages
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until Ctrl-C is pressed
    updater.idle()

if __name__ == '__main__':
    main()
