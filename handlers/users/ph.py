
from aiogram import types
from aiogram.types import ContentType, InputFile, document
from loader import bot

from loader import dp



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.answer(message.text)



@dp.message_handler(text='PHP darslari')
async def bot_echo(message: types.Message):
        await message.reply_document(document='https://t.me/lksdjfgs/80')#1
        await message.reply_document(document='https://t.me/lksdjfgs/81')#2
        await message.reply_document(document='https://t.me/lksdjfgs/82')#3
        await message.reply_document(document='https://t.me/lksdjfgs/83')#4
        await message.reply_document(document='https://t.me/lksdjfgs/84')#5
        await message.reply_document(document='https://t.me/lksdjfgs/85')#6
        await message.reply_document(document='https://t.me/lksdjfgs/86')#7
        await message.reply_document(document='https://t.me/lksdjfgs/87')#8
        await message.reply_document(document='https://t.me/lksdjfgs/88')#9
        await message.reply_document(document='https://t.me/lksdjfgs/89')#10
        await message.reply_document(document='https://t.me/lksdjfgs/90')#11
        await message.reply_document(document='https://t.me/lksdjfgs/91')#12
        await message.reply_document(document='https://t.me/lksdjfgs/92')#13
        await message.reply_document(document='https://t.me/lksdjfgs/93')#14
        await message.reply_document(document='https://t.me/lksdjfgs/94')#15