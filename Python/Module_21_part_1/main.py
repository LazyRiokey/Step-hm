import json
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.dispatcher.filters import Text

bot = Bot("5524861093:AAGxh2PWUY7UqtJdcS4PQtgMMgSSsD8aZ8k")
dp = Dispatcher(bot)


def get_random_data(command: str):
    with open(".\\literature\\literature_datа.json", "r", encoding="utf8") as raw_json:
        raw_data = json.load((raw_json))

    """ Очень не нравится мне это решение, но не могу сообразить,
    как код сделать более компактным, без особых повторений.."""

    random_writer = [*raw_data[0]["Writers"].keys()][random.randint(0, 4)]
    random_poets = [*raw_data[0]["Poets"].keys()][random.randint(0, 4)]

    if command == "/Писатель":
        return random_writer
    elif command == "/Поэт":
        return random_poets
    elif command == "/Книга":
        return random_writer, raw_data[0]["Writers"][random_writer][random.randint(0, 1)],
    elif command == "/Стих":
        return random_poets, raw_data[0]["Poets"][random_poets][random.randint(0, 3)]
    else:
        return None


@dp.message_handler(commands=["Писатель", "Поэт", "Книга", "Стих"])
async def task_4(message: types.Message):
    try:
        command = message.get_command()
        info = get_random_data((command))
        if command == "/Писатель":
            await message.answer(f"Случайные писатель:\n{info}")
        elif command == "/Поэт":
            await message.answer(f"Случайный поэт:\n{info}")
        elif command == "/Книга":
            await message.answer(f"Писатель: {info[0]}\nКнига: {info[1]}")
        elif command == "/Стих":
            await message.answer(f"Поэт: {info[0]}\nСтихотворение: {info[1]}")
    except:
        await message.answer("Что-то пошло не так..")


executor.start_polling(dp, skip_updates=True)
