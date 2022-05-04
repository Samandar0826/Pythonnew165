
from aiogram import types
from aiogram.types import ContentType, InputFile, document
from loader import bot

from loader import dp



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.answer(message.text)



@dp.message_handler(text='3Ds max darslari')
async def bot_echo(message: types.Message):
        await message.reply_document(document='https://t.me/lksdjfgs/18')#1
        await message.reply_document(document='https://t.me/lksdjfgs/19')#2
        await message.reply_document(document='https://t.me/lksdjfgs/20')#3
        await message.reply_document(document='https://t.me/lksdjfgs/21')#4
        await message.reply_document(document='https://t.me/lksdjfgs/22')#5
        await message.reply_document(document='https://t.me/lksdjfgs/23')#6
        await message.reply_document(document='https://t.me/lksdjfgs/24')#7
        await message.reply_document(document='https://t.me/lksdjfgs/25')#8
        await message.reply_document(document='https://t.me/lksdjfgs/26')#9
        await message.reply_document(document='https://t.me/lksdjfgs/27')#10
        await message.reply_document(document='https://t.me/lksdjfgs/28')#11
        await message.reply_document(document='https://t.me/lksdjfgs/29')#12
        await message.reply_document(document='https://t.me/lksdjfgs/30')#13
        await message.reply_document(document='https://t.me/lksdjfgs/31')#14
        await message.reply_document(document='https://t.me/lksdjfgs/32')#15