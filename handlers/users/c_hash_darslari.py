
from aiogram import types
from aiogram.types import ContentType, InputFile, document
from loader import bot

from loader import dp



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.answer(message.text)



@dp.message_handler(text='C# darslari')
async def bot_echo(message: types.Message):
        await message.reply_document(document='https://t.me/lksdjfgs/108')#1
        await message.reply_document(document='https://t.me/lksdjfgs/109')#2
        await message.reply_document(document='https://t.me/lksdjfgs/110')#3
        await message.reply_document(document='https://t.me/lksdjfgs/111')#4
        await message.reply_document(document='https://t.me/lksdjfgs/112')#5
        await message.reply_document(document='https://t.me/lksdjfgs/113')#6
        await message.reply_document(document='https://t.me/lksdjfgs/114')#7
        await message.reply_document(document='https://t.me/lksdjfgs/115')#8
        await message.reply_document(document='https://t.me/lksdjfgs/116')#9
        await message.reply_document(document='https://t.me/lksdjfgs/117')#10
        await message.reply_document(document='https://t.me/lksdjfgs/119')#11
        await message.reply_document(document='https://t.me/lksdjfgs/120')#12
        await message.reply_document(document='https://t.me/lksdjfgs/121')#13
        await message.reply_document(document='https://t.me/lksdjfgs/122')#14
        await message.reply_document(document='https://t.me/lksdjfgs/123')#15