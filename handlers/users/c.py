from aiogram import types


from loader import dp
from keyboards.default.ccc import python_c



# Echo bot
@dp.message_handler(text='C++ 👨‍💻')
async def bot_echo(message: types.Message):
    await message.answer(text='Darslar',  reply_markup=python_c)
