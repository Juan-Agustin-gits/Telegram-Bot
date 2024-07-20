from telegram import Update
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import photos, random
import os
def randomNumber(listPhotos: photos.fotos):
    max = len(listPhotos)-1
    min = 0


    number = random.randint(min,max)
    return number




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text ="Hola Anto este es un bot que estoy creando para hacer pruebas")





async def anto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photosAnto = photos.fotos
    index = randomNumber(photosAnto)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photosAnto[index])
    await context.bot.send_message(chat_id=update.effective_chat.id, text ="Te Quiero <3")

def main():
    load_dotenv()
    token = os.getenv('TELEGRAM-TOKEN')
    application = ApplicationBuilder().token(token).build()
    start_comand = CommandHandler('start', start)
    anto_comand = CommandHandler('Anto', anto)
    application.add_handler(start_comand)
    application.add_handler(anto_comand)


    application.run_polling()

### llamamos a la funcion  main para correr todo el programa 
main()