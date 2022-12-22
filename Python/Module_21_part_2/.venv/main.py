from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot("5524861093:AAGxh2PWUY7UqtJdcS4PQtgMMgSSsD8aZ8k")
dp = Dispatcher(bot)


COACHES = {
    "coach 1": "information about coach 1",
    "coach 2": "information about coach 2",
    "coach 3": "information about coach 3",
    "coach 4": "information about coach 4",
    "coach 5": "information about coach 5",
    "coach 6": "information about coach 6"
}

GROUPS = {
    "Group lesson 1": "information about group lesson 1",
    "Group lesson 2": "information about group lesson 2",
    "Group lesson 3": "information about group lesson 3",
    "Group lesson 4": "information about group lesson 4",
    "Group lesson 5": "information about group lesson 5",
    "Group lesson 6": "information about group lesson 6",
}

# 1

@dp.callback_query_handler(text=[*COACHES.keys()])
async def get_info_about_coaches(callback: types.CallbackQuery):
    await callback.message.answer(COACHES.get(callback.data))
    await callback.answer()


@dp.message_handler(commands=["coaches"])
async def get_coaches(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=3)
    buttons = []
    for key in COACHES.keys():
        buttons.append(InlineKeyboardButton(text=key, callback_data=key))
    kb.add(*buttons)
    await message.answer(text="Список всех тренеров:", reply_markup=kb)

# 2

@dp.callback_query_handler(text=[*GROUPS.keys()])
async def get_info_about_groups(callback: types.CallbackQuery):
    await callback.message.answer(GROUPS.get(callback.data))
    await callback.answer()


@dp.message_handler(commands=["groups"])
async def get_groups(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=3)
    buttons = []
    for key in GROUPS.keys():
        buttons.append(InlineKeyboardButton(text=key, callback_data=key))
    kb.add(*buttons)
    await message.answer(text="Список всех груп:", reply_markup=kb)

# 3

@dp.message_handler(commands=["today"])
async def get_today_group(message: types.Message):
    for key, value in GROUPS.items():
        await message.answer(text=f"Занятие на сегодня\n{key} : {value}")
        break

# 4

@dp.message_handler(commands=["week"])
async def get_week_groups(message: types.Message):
    groups = ""
    for key, value in GROUPS.items():
        groups += f"{key} : {value}\n"
    await message.answer(text=groups)

executor.start_polling(dp, skip_updates=True)
