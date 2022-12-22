from email import message
import json
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text


bot = Bot("5524861093:AAGxh2PWUY7UqtJdcS4PQtgMMgSSsD8aZ8k")
dp = Dispatcher(bot)


# b1 = KeyboardButton(text="/all")
# b2 = KeyboardButton(text="/theater")
# b3 = KeyboardButton(text="/concert")
# b4 = KeyboardButton(text="Поделиться контактом", request_contact=True)
# kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# kb.add(b1).row(b2, b3).row(b4)


# kb = InlineKeyboardMarkup(row_width=2)
# b1 = InlineKeyboardButton(text="Google", url="https://www.google.com/")
# b2 = InlineKeyboardButton(text="Клик", callback_data="click")

# kb.add(b1, b2)


# @dp.callback_query_handler(text="click")
# async def click_button(callback: types.CallbackQuery):
#     await callback.message.answer("Вы кликнули по кнопке!")
#     await callback.answer()


# @dp.message_handler(commands=["start"])
# async def start_func(message: types.Message):
#     try:
#         await message.answer("Добрый день..", reply_markup=kb)
#     except:
#         await message.answer("Что-то пошло не так..")



kb = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text="За", callback_data="1")
b2 = InlineKeyboardButton(text="Против", callback_data="-1")

kb.add(b1, b2)

users = {}

@dp.callback_query_handler(Text(endswith="1"))
async def click_button(callback: types.CallbackQuery):
    result = int(callback.data)
    if callback.from_user.id not in users.keys():
        users[callback.from_user.id] = result
        await callback.answer("Вы проголосовали!")
    else:
        await callback.answer("Вы уже проголосовали!")



@dp.message_handler(commands=["start"])
async def start_func(message: types.Message):
    try:
        await message.answer("Начинаем голосование..", reply_markup=kb)
    except:
        await message.answer("Что-то пошло не так..")



# @dp.message_handler()
# async def task_3(message: types.Message):
#     MESS_ANSW_DICT = {
#         "Привет": "Привет!",
#         "Как дела?": "Прекрасно!",
#         "Расскажи о себе": "Я тестовый бот...",
#         "Пока": "Пока!",
#         "Hi": "Hi!",
#         "How are you?": "Fine. Thanks!",
#         "Tell me about you": "I am a test bot...",
#         "Bye": "Bye!",
#     }
#     try:
#         if message.text in MESS_ANSW_DICT.keys():
#             await message.answer(MESS_ANSW_DICT.get(message.text))
#         else:
#             await message.answer("Я не знаю такой команды..")
#     except:
#         await message.answer("Что-то пошло не так..")


# @dp.message_handler(commands=["date", "theater", "concert", "all"])
# async def task_4(message: types.Message):
#     try:
#         with open(".\\theater\\events.json", "r") as raw_json:
#             raw_data = json.load(raw_json)

#         cur_events = ""
#         command = message.get_command()
#         for item in raw_data:
#             if command == "/date":
#                 if message.get_args() in item.values():
#                     cur_events += "Дата: {date}\nТеатр: {theater}\nКонцерты: {concert}\n\n".format(**item)
#             elif command == "/theater":
#                     cur_events += "Дата: {date}\nТеатр: {theater}\n\n".format(**item)
#             elif command == "/concert":
#                 cur_events += "Дата: {date}\nКонцерты: {concert}\n\n".format(**item)
#             elif command == "/all":
#                 cur_events += "Дата: {date}\nТеатр: {theater}\nКонцерты: {concert}\n\n".format(**item)
#             else:
#                 await message.reply("Команда не распознана..")
#         await message.answer(cur_events, reply_markup=kb)
#     except:
#         await message.answer("Что-то пошло не так..")


executor.start_polling(dp, skip_updates=True)
