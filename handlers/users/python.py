from aiogram import types

from keyboards.default.video_darslar import asosiy_menu
from loader import dp
from keyboards.default.python_tugma import python_s





# Echo bot
@dp.message_handler(text='Python 🐍')
async def bot_echo(message: types.Message):
    await message.answer(text='darslar',  reply_markup=python_s)



@dp.message_handler(text='Orqaga')
async def bot_echo(message: types.Message):
    await message.answer(text='Orqaga',reply_markup=asosiy_menu)







