from aiogram import types


from loader import dp
from keyboards.default.frontend import python_f



# Echo bot
@dp.message_handler(text='Front-end 👨‍💻')
async def bot_echo(message: types.Message):
    await message.answer(text='Darslar',  reply_markup=python_f)
