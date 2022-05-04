from aiogram import types


from loader import dp
from keyboards.default.smm import python_s



# Echo bot
@dp.message_handler(text='SMM ✅')
async def bot_echo(message: types.Message):
    await message.answer(text='Darslar',  reply_markup=python_s)
