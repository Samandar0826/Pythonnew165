from aiogram import types


from loader import dp
from keyboards.default.max import python_m



# Echo bot
@dp.message_handler(text='3Ds Max 🏠')
async def bot_echo(message: types.Message):
    await message.answer(text='Darslar',  reply_markup=python_m)
