from aiogram import types


from loader import dp
from keyboards.default.java import python_j



# Echo bot
@dp.message_handler(text='Java script ☕')
async def bot_echo(message: types.Message):
    await message.answer(text='Darslar',  reply_markup=python_j)
