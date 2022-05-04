
from aiogram import types
from aiogram.types import ContentType, InputFile, document
from loader import bot

from loader import dp



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.answer(message.text)



@dp.message_handler(text='Android dasturlash darslari')
async def bot_echo(message: types.Message):
        await message.reply_document(document='https://t.me/lksdjfgs/124')#1
        await message.reply_document(document='https://t.me/lksdjfgs/125')#2
        await message.reply_document(document='https://t.me/lksdjfgs/126')#3
        await message.reply_document(document='https://t.me/lksdjfgs/127')#4
        await message.reply_document(document='https://t.me/lksdjfgs/128')#5
        await message.reply_document(document='https://t.me/lksdjfgs/129')#6
        await message.reply_document(document='https://t.me/lksdjfgs/130')#7
        await message.reply_document(document='https://t.me/lksdjfgs/131')#8
        await message.reply_document(document='https://t.me/lksdjfgs/132')#9
        await message.reply_document(document='https://t.me/lksdjfgs/133')#10
        await message.reply_document(document='https://t.me/lksdjfgs/134')#11
        await message.reply_document(document='https://t.me/lksdjfgs/135')#12
        await message.reply_document(document='https://t.me/lksdjfgs/136')#13
        await message.reply_document(document='https://t.me/lksdjfgs/137')#14
        await message.reply_document(document='https://t.me/lksdjfgs/138')#15