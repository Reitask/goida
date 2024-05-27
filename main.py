from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id, "СВО Слава Богу 🙏❤️СЛАВА СВО 🙏❤️АНГЕЛА ХРАНИТЕЛЯ СВО 🙏❤️БОЖЕ ХРАНИ СВО 🙏❤️СПАСИБО СВО 🙏🏼❤️🇷🇺 ЧТО ПОДДЕРЖИМ СВО🙏❤️Слава Богу СВО 🙏❤️СЛАВА СВО 🙏❤️ГОЙДА")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())