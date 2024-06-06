import asyncio
import json

from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.filters import Command, CommandStart, StateFilter, or_f


from config import TOKEN

bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton(text='Открыть Веб страницу', web_app=WebAppInfo(url='https://github.com/Bylba4kka/tg_bot_web_app'))]
    ])
    await message.answer("Привет!", reply_markup=markup)


@dp.message(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.load(message.web_app_data.data)
    await message.answer(f"Имя: {res['name']}\nПочта: {res['email']}\nТелефон\n{res['phone']}")


async def main():

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())