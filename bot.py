import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    update.message.reply_text("Hola, Panarra!")


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def help(update, context):
    update.message.reply_text("Estos son los comandos que puedes usar para hacer tu pan casero:")
    update.message.reply_text("/ayuda")
    update.message.reply_text("/help")
    update.message.reply_text("/new")
    update.message.reply_text("/nuevo")


def main():
    """Inicio del Bot"""
    # Colocamos el Token creado por FatherBot
    updater = Updater(os.environ['TOKEN'], use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("ayuda", help))
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

