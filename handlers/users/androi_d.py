from aiogram import types


from loader import dp
from keyboards.default.android import python_a



# Echo bot
@dp.message_handler(text='Android 📱')
async def bot_echo(message: types.Message):
    await message.answer(text='Darslar',  reply_markup=python_a)
