import asyncio
import logging
from aiogram import Bot, Dispatcher, Router
import openpyxl
from aiogram.filters.command import Command
from aiogram.types import Message
from root import TOKEN

bot = Bot(token=TOKEN)

dp = Dispatcher()

rt = Router
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet["A1"] = "Name"
sheet["B1"] = "Card"


@dp.message(Command("start"))
async def start(message: Message):
    await message.reply(f"Salom {message.from_user.full_name}!")
    print(f"Id:{message.from_user.id}")

    sheet["A2"] = message.from_user.full_name
    sheet["B2"] = message.from_user.id

    workbook.save("dates.xlsx")


async def main():
    await dp.start_polling(bot)


if main == "main":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
