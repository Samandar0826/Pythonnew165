
from aiogram import types
from aiogram.types import ContentType, InputFile, document
from loader import bot

from loader import dp



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.answer(message.text)



@dp.message_handler(text='Front-end darslari')
async def bot_echo(message: types.Message):
        await message.reply_document(document='https://t.me/lksdjfgs/67')#1
        await message.reply_document(document='https://t.me/lksdjfgs/68')#2
        await message.reply_document(document='https://t.me/lksdjfgs/69')#3
        await message.reply_document(document='https://t.me/lksdjfgs/70')#4
        await message.reply_document(document='https://t.me/lksdjfgs/71')#5
        await message.reply_document(document='https://t.me/lksdjfgs/72')#6
        await message.reply_document(document='https://t.me/lksdjfgs/73')#7
        await message.reply_document(document='https://t.me/lksdjfgs/74')#8
        await message.reply_document(document='https://t.me/lksdjfgs/75')#9
        await message.reply_document(document='https://t.me/lksdjfgs/76')#10
        await message.reply_document(document='https://t.me/lksdjfgs/77')#11
        await message.reply_document(document='https://t.me/lksdjfgs/78')#12
        await message.reply_document(document='https://t.me/lksdjfgs/79')#13
