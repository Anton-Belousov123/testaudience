import json
import logging
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor


def get_rows():
    plaques = json.load(open('buttons.json', 'r', encoding='UTF-8'))
    print(plaques)
    elms = sorted(plaques, key=lambda k: k['y'])
    start_y = elms[0]['y']
    res = [[elms[0]]]
    print(start_y)
    for elm in elms[1::]:
        if start_y + 30 < elm['y']:
            res.append([])
            start_y = elm['y']
        res[-1].append(elm)
    for row in range(len(res)):
        res[row] = sorted(res[row], key=lambda k: k['x'])
    return res


def get_keyboard():
    rows = get_rows()
    keyboard = InlineKeyboardMarkup()
    for row in rows:
        btns = []
        for col in row:
            btns.append(InlineKeyboardButton(col['name'], callback_data='b'))
        keyboard.add(*btns)

    return keyboard



logging.basicConfig(level=logging.INFO)

API_TOKEN = '6249648276:AAEXbDIDX8fa4q13a88L1lQv6vQGDkvXZD0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = get_keyboard()
    print(keyboard)
    await message.reply("Hi, I'm a bot!", reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
