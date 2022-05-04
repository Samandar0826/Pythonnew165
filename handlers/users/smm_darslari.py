
from aiogram import types
from aiogram.types import ContentType, InputFile, document
from loader import bot

from loader import dp



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.answer(message.text)



@dp.message_handler(text='SMM darslari')
async def bot_echo(message: types.Message):
        await message.reply_document(document='https://t.me/lksdjfgs/95')#1
        await message.reply_document(document='https://t.me/lksdjfgs/96')#2
        await message.reply_document(document='https://t.me/lksdjfgs/97')#3
        await message.reply_document(document='https://t.me/lksdjfgs/98')#4
        await message.reply_document(document='https://t.me/lksdjfgs/100')#5
        await message.reply_document(document='https://t.me/lksdjfgs/101')#6
        await message.reply_document(document='https://t.me/lksdjfgs/102')#7
        await message.reply_document(document='https://t.me/lksdjfgs/103')#8
        await message.reply_document(document='https://t.me/lksdjfgs/104')#9
        await message.reply_document(document='https://t.me/lksdjfgs/105')#10
        await message.reply_document(document='https://t.me/lksdjfgs/106')#11

