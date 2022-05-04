from aiogram import types


from loader import dp
from keyboards.default.PHP import python_p



# Echo bot
@dp.message_handler(text='PHP ✅')
async def bot_echo(message: types.Message):
    await message.answer(text='Darslar',  reply_markup=python_p)
