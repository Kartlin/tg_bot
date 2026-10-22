import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup    
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)
from datetime import datetime
import random

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

app = ApplicationBuilder().token(TOKEN).build()

async def start(update, context):
    button_hi = KeyboardButton("привемба")
    button_how = KeyboardButton("какделамба") 
    button_help = KeyboardButton("помогитемне")

    keyboard = [[button_hi, button_how], [button_help]]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text('Выберите Опцию:', reply_markup=reply_markup)


async def help_command(update, context):
    await update.message.reply_text(
        "Команды: \n/start - начать\n/help - помощь\n/about - обо мне"
    )

async def about(update, context):
    await update.message.reply_text(
        'Для тех, кто не знает, что такое бипки\n/Стоят пассажиры в аэропорту, посадочный досмотр проходят. Дошла очередь до мужика с чемоданом.\n/— Пожалуйста, приготовьте чемодан к осмотру.\n/— Не могу.\n/— Почему?\n/— А у меня там бипки!\n/— А что это?\n/— Ну, отсосёте — покажу!\n/Служба безопасности шутку не поняла, вызвала наряд полиции:\n/— Гражданин, открывайте чемодан.\n/— Но я не могу!\n/— Почему не можете?\n/— Потому что у меня там бипки!\n/— «Бипки»? Что это?\n/— Так отсосите мне, и я покажу!\n/Отобрали чемодан, а открыть никто не может. Повезли мужика в СИЗО. В камере сидельцы расспрашивают:\n/— Братуха, за что тебя?\n/— Да чемодан отказался открывать.\n/— А что там?\n/— Да бипки там.\n/— Какие нахуй «бипки»?\n/— Ну отсосите мне, тогда и расскажу\n/И вот угодил мужик в лазарет, с побоями да синяками по всему телу, весь перебинтован, еле дышит. \n/ Следователи вызвали группу специалистов для вскрытия чемодана. \n/ Час, два, три пыхтели. Кое-как разворотили, смотрят — а там \n/ бипки.'
    )

async def menu(update, context):
    button_time = InlineKeyboardButton("Дата и время", callback_data="time")
    button_fact = InlineKeyboardButton("Случайный факт", callback_data="fact")
    button_site = InlineKeyboardButton("Открыть сайт", url="https://example.com")
    keyboard = [
        [button_time, button_fact],
        [button_site]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите действие:", reply_markup=reply_markup)

async def button_callback(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "time":
        now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        await query.edit_message_text(f"Текущее время: {now}")
    elif query.data == "fact":
        facts = ["Коты спят 70% жизни.", "Банан — это ягода.", "У улиток 14 000 зубов."]
        await query.edit_message_text(random.choice(facts))

async def handle_text(update, context):
    text = update.message.text

    if text == "привемба":
        await update.message.reply_text("Привет!")
    elif text == "какделамба":
        await update.message.reply_text("Нормально! А у тебя как?")
    elif text == "помогитемне":
        await update.message.reply_text("Напиши /help")
    else:
        await update.message.reply_text("Не понимаю такую команду")


app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('about', about))
app.add_handler(CommandHandler('menu', menu))

app.add_handler(CallbackQueryHandler(button_callback))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

if __name__ == '__main__':
    app.run_polling()


    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('about', about))
    app.add_handler(CommandHandler('menu', menu))

if __name__ == '__main__':
    app.run_polling()





