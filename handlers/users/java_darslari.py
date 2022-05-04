
from aiogram import types
from aiogram.types import ContentType, InputFile, document
from loader import bot

from loader import dp



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.answer(message.text)



@dp.message_handler(text='Java script darslari')
async def bot_echo(message: types.Message):
        await message.reply_document(document='https://t.me/lksdjfgs/35')#1
        await message.reply_document(document='https://t.me/lksdjfgs/37')#2
        await message.reply_document(document='https://t.me/lksdjfgs/38')#3
        await message.reply_document(document='https://t.me/lksdjfgs/39')#4
        await message.reply_document(document='https://t.me/lksdjfgs/40')#5
        await message.reply_document(document='https://t.me/lksdjfgs/41')#6
        await message.reply_document(document='https://t.me/lksdjfgs/42')#7
        await message.reply_document(document='https://t.me/lksdjfgs/43')#8
        await message.reply_document(document='https://t.me/lksdjfgs/44')#9
        await message.reply_document(document='https://t.me/lksdjfgs/45')#10
        await message.reply_document(document='https://t.me/lksdjfgs/46')#11
        await message.reply_document(document='https://t.me/lksdjfgs/47')#12
        await message.reply_document(document='https://t.me/lksdjfgs/48')#13
        await message.reply_document(document='https://t.me/lksdjfgs/49')#14
        await message.reply_document(document='https://t.me/lksdjfgs/50')#15