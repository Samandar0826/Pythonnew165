
from aiogram import types
from aiogram.types import ContentType, InputFile, document
from loader import bot

from loader import dp



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.answer(message.text)



@dp.message_handler(text='Python darslari')
async def bot_echo(message: types.Message):
        await message.reply_document(document='https://t.me/lksdjfgs/16')#1
        await message.reply_document(document='https://t.me/lksdjfgs/15')#2
        await message.reply_document(document='https://t.me/lksdjfgs/14')#3
        await message.reply_document(document='https://t.me/lksdjfgs/13')#4
        await message.reply_document(document='https://t.me/lksdjfgs/12')#5
        await message.reply_document(document='https://t.me/lksdjfgs/11')#6
        await message.reply_document(document='https://t.me/lksdjfgs/10')#7
        await message.reply_document(document='https://t.me/lksdjfgs/9')#8
        await message.reply_document(document='https://t.me/lksdjfgs/8')#9
        await message.reply_document(document='https://t.me/lksdjfgs/7')#10
        await message.reply_document(document='https://t.me/lksdjfgs/6')#11
        await message.reply_document(document='https://t.me/lksdjfgs/5')#12
        await message.reply_document(document='https://t.me/lksdjfgs/4')#13
        await message.reply_document(document='https://t.me/lksdjfgs/3')#14
        await message.reply_document(document='https://t.me/lksdjfgs/2')#15