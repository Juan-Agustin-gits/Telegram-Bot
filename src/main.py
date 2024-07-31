from telegram import Update
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import photos, random, time_RS, connectionBD
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

async def request_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_request ="Ingresa el titulo de tu Cita: "
    title = ""
    await context.bot.send_message(chat_id=update.effective_chat.id, text =text_request)
    title = update.message.text
    print(title)
    ##await context.bot.
async def addDate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for i in range(1,5):
        if i == 1:
            await request_title
        elif i == 2:
            break
            print()
        elif i == 3:
            print()
        elif i == 4:
            print()
        elif i == 5:
            print()
async def time_relationShip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    time = str(time_RS.time_relationShip())
    string = f"Llevamos: { time } segundos"
    await context.bot.send_message(chat_id=update.effective_chat.id, text =string)

def main():
    load_dotenv()
    token = os.getenv('TELEGRAM-TOKEN')
    application = ApplicationBuilder().token(token).build()
    start_command = CommandHandler('start', start)
    anto_command = CommandHandler('Anto', anto)
    time_command = CommandHandler('pololeo', time_relationShip)
    date_command = CommandHandler('Cita', addDate)
    application.add_handler(start_command)
    application.add_handler(anto_command)
    application.add_handler(time_command)
    application.add_handler(date_command)



    application.run_polling()

### llamamos a la funcion  main para correr todo el programa 
main()