from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Inserisci il tuo token qui
TOKEN = '7900779724:AAGRMdBk-z-54Y4Y_gtSvJgSgPHnTffs2Ig'

# Funzione per gestire il comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Ciao! Sono il tuo bot Aviator. Inviami un comando per iniziare!')

# Impostazione del bot
def main():
    # Crea l'applicazione del bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Aggiungi il comando /start
    app.add_handler(CommandHandler('start', start))

    # Avvia il bot
    app.run_polling()

if __name__ == '__main__':
    main()
