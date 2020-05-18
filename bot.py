from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    update.message.reply_text("Hola, Panarra!")


def main():
    """Inicio del Bot"""
    # Colocamos el Token creado por FatherBot
    updater = Updater("932726420:AAE9Y0sNlgTG9_VOwAtJkU1DaodvFs4PLwI", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", help))
    # dp.add_handler(CommandHandler("mayus", mayus))
    #
    # dp.add_handler(MessageHandler(Filters.text, alreves))

    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    #

    # Y este espera al error
    # dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

