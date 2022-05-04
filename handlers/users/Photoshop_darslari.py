
from aiogram import types
from aiogram.types import ContentType, InputFile, document
from loader import bot

from loader import dp



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.answer(message.text)



@dp.message_handler(text='Photoshop darslari')
async def bot_echo(message: types.Message):
        await message.reply_document(document='https://t.me/lksdjfgs/139')#1
        await message.reply_document(document='https://t.me/lksdjfgs/140')#2
        await message.reply_document(document='https://t.me/lksdjfgs/141')#3
        await message.reply_document(document='https://t.me/lksdjfgs/142')#4
        await message.reply_document(document='https://t.me/lksdjfgs/143')#5
        await message.reply_document(document='https://t.me/lksdjfgs/144')#6
        await message.reply_document(document='https://t.me/lksdjfgs/145')#7
        await message.reply_document(document='https://t.me/lksdjfgs/146')#8
        await message.reply_document(document='https://t.me/lksdjfgs/147')#9
        await message.reply_document(document='https://t.me/lksdjfgs/148')#10
        await message.reply_document(document='https://t.me/lksdjfgs/149')#11
        await message.reply_document(document='https://t.me/lksdjfgs/150')#12
        await message.reply_document(document='https://t.me/lksdjfgs/151')#13
        await message.reply_document(document='https://t.me/lksdjfgs/152')#14
        await message.reply_document(document='https://t.me/lksdjfgs/153')#15