import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from Keyboard import get_keyboard
from UserStates import UserStates

from Keyboard import keyboards
import services.in_memory_pari_service as ps
from config import TOKEN

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)

@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    kb = get_keyboard()
    await message.answer("Привет, я простой эхо-бот", reply_markup=kb)
    await state.set_state(UserStates.BASE)


@dp.message(Command("test"), StateFilter(UserStates.BASE))
async def start(message: types.Message):
    kb = keyboards[UserStates.BASE]
    paris = ps.get_pari_by_user_id(message.from_user.id)
    if len(paris) == 0:
        answer_text = "У тебя нет пари"
    else:
        i = 1
        answer_text = "Твои пари:"
        for pari in paris:
            answer_text += "\n" + str(i) + ") " + pari
            i+=1
    await message.answer(answer_text, reply_markup=kb)
    await message.answer("Ты в состоянии BASE")
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
