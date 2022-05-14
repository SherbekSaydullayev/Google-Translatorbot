import logging
from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
from buttons import til1,boshlash,boshlash1
from aiogram.types import CallbackQuery
import sqlite3
from classlar import Sql

 ## vaqtni topish 
# from datetime import datetime
# import pytz


# IST = pytz.timezone('Asia/Samarkand')

# datetime_ist = datetime.now(IST)
# sana = datetime_ist.strftime('%Y-%m-%d %H:%M:%S')


logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
x = Translator()
db = Sql()
Admin = 1168299390

        
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    db.baza_create()
    global user_id
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    data1 = db.user_id(user_id)
    if data1 is None:
        db.user_add(user_id,username,first_name)
        await message.reply(f"<strong>{message.from_user.full_name} 🇺🇿Botga xush kelibsiz,Matnni istalgan tilda kiriting, biz uni istalgan tilga tarjima qilamiz!  </strong>"
            f"\n \n <strong>{message.from_user.full_name} 🇷🇺Добро пожаловать в наш бот, Введите любой текст на любом языке мы его переведем в любой доступный язык! </strong>"
            f"<strong>\n \n 🏴󠁧󠁢󠁥󠁮󠁧󠁿Hello {message.from_user.full_name}, Enter text in any language, we will translate it into any available language!</strong>"
            f"<strong>\n \n {message.from_user.full_name} 🇸🇦رحبًا بك في الروبوت ، أدخل النص بأي لغة ، وسنقوم بترجمته إلى أي لغة </strong>",parse_mode='HTML',reply_markup=boshlash)
        await bot.send_message(Admin,f"Ro'yxatga qo'shildi: \nusername: @{message.from_user.username}\nfirstname: {message.from_user.first_name}\nid: {message.from_user.id}")
    else:
        await message.reply(f"<strong>🇺🇿 So'z kiriting</strong>"
        f"\n<strong>🇷🇺 Введите слово</strong>"
        f"\n<strong>🏴󠁧󠁢󠁥󠁮󠁧󠁿 Enter the word</strong>"
        f"\n<strong>🇸🇦 أدخل الكلمة</strong>",parse_mode = 'HTML')

@dp.callback_query_handler(text = "boshlash1")
async def fo(call:CallbackQuery):
    await call.message.answer(f"<strong>🇺🇿 So'z kiriting</strong>"
        f"\n<strong>🇷🇺 Введите слово</strong>"
        f"\n<strong>🏴󠁧󠁢󠁥󠁮󠁧󠁿 Enter the word</strong>"
        f"\n<strong>🇸🇦 أدخل الكلمة</strong>",parse_mode = 'HTML')
## Foydalanuvchilar soni
@dp.message_handler(commands=['alluser'],user_id = 1168299390)
async def send_welcome(message: types.Message):
    fo1 = db.sana()
    for i in fo1:
        b = i[0]
        await message.reply(f"Foydalanuvchilar soni {b} ta")

#### REKLAMA###
@dp.message_handler(commands=['reklama'],user_id = 1168299390)
async def send_welcome(message: types.Message):
    rek1 = db.reklama()
    for j in rek1:
        user_id = j[0]
        await bot.send_message(chat_id = user_id,text = f"Assalom aleykum obunachilarimiz Sizlarga tavsiya qilib qolamiz\nKreativni motivatsiyali kanal kirib ko'rishingiz mumkin\nSizlarga yoqadigan umidaman\nKanal: https://t.me/sherbekblog")
    

@dp.message_handler()
async def echo(message: types.Message):
    global soz
    soz = message.text
    await message.answer(f"<b>🇺🇿 Tillarni tanlang!</b>"
        f"\n \n<b>🇷🇺 Выберите языки!</b>"
        f"\n \n<b>🏴󠁧󠁢󠁥󠁮󠁧󠁿 Select languages! </b>"
        f"\n \n <b>🇸🇦 رحدد اللغات</b>",parse_mode='HTML',reply_markup = til1)

## 1-tillar
@dp.callback_query_handler(text = "af")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "af" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "sq")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "sq" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "hy")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "hy" )
    await call.message.answer(tarjima.text)

## 2-tillar
@dp.callback_query_handler(text = "ar")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "ar" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "az")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "az" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "be")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "be" )
    await call.message.answer(tarjima.text)

## 3-tillar
@dp.callback_query_handler(text = "bn")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "bn" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "bs")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "bs" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "bg")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "bg" )
    await call.message.answer(tarjima.text)

## 4-tillar
@dp.callback_query_handler(text = "hr")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "hr" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "cs")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "cs" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "en")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "en" )
    await call.message.answer(tarjima.text)

## 5-tillar
@dp.callback_query_handler(text = "et")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "et" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "fr")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "fr" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "ka")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "ka" )
    await call.message.answer(tarjima.text)
## 6-tillar
@dp.callback_query_handler(text = "de")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "de" )
    await call.message.answer(tarjima.text)
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "hi")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "hi" )
    await call.message.answer(tarjima.text)
## 7-tillar
@dp.callback_query_handler(text = "hu")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "hu" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "id")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "id" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "is")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "is" )
    await call.message.answer(tarjima.text)
## 8-tillar
@dp.callback_query_handler(text = "it")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "it" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "ja")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "ja" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "kn")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "kn" )
    await call.message.answer(tarjima.text)
## 9-tillar
@dp.callback_query_handler(text = "kk")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "kk" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "ky")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "ky" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "ko")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "ko" )
    await call.message.answer(tarjima.text)
## 10-tillar
@dp.callback_query_handler(text = "lv")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "lv" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "mk")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "mk" )
    await call.message.answer(tarjima.text)

## 11-tillar
@dp.callback_query_handler(text = "ms")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "ms" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "mn")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "mn" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "ne")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "ne" )
    await call.message.answer(tarjima.text)


## 12-tillar
@dp.callback_query_handler(text = "no")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "no" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "pl")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "pl" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "pt")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "pt" )
    await call.message.answer(tarjima.text)

## 13-tillar
@dp.callback_query_handler(text = "ro")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "ro" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "ru")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "ru" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "sr")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "sr" )
    await call.message.answer(tarjima.text)

## 14-tillar
@dp.callback_query_handler(text = "sk")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "sk" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "sl")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "sl" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "es")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "es" )
    await call.message.answer(tarjima.text)

## 15-tillar
@dp.callback_query_handler(text = "sv")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "sv" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "tg")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "tg" )
    await call.message.answer(tarjima.text)

## 16-tillar
@dp.callback_query_handler(text = "tr")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "tr" )
    await call.message.answer(tarjima.text)


## 17-tillar
@dp.callback_query_handler(text = "uk")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "uk" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "ur")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "ur" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "uz")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "uz")
    await call.message.answer(tarjima.text)


## 18-tillar
@dp.callback_query_handler(text = "vi")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "vi" )
    await call.message.answer(tarjima.text)
@dp.callback_query_handler(text = "zh-cn")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "zh-cn" )
    await call.message.answer(tarjima.text)         
@dp.callback_query_handler(text = "el")
async def fo(call:CallbackQuery):
    tarjima = x.translate(soz, dest = "el" )
    await call.message.answer(tarjima.text)         

# @dp.callback_query_handler(text = "")
# async def fo(call:CallbackQuery):
#     tarjima = x.translate(soz, dest = "" )
#     await call.message.answer(tarjima.text)

        # Baza dannix







if __name__ == '__main__':
     executor.start_polling(dp, skip_updates=True)
