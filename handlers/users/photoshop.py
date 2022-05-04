from aiogram import types


from loader import dp
from keyboards.default.photo_shop import python_ph



# Echo bot
@dp.message_handler(text='Photoshop 🖼')
async def bot_echo(message: types.Message):
    await message.answer(text='Darslar',  reply_markup=python_ph)
