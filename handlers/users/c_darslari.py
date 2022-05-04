
from aiogram import types
from aiogram.types import ContentType, InputFile, document
from loader import bot

from loader import dp



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.answer(message.text)



@dp.message_handler(text='C++ darslari')
async def bot_echo(message: types.Message):
        await message.reply_document(document='https://t.me/lksdjfgs/51')#1
        await message.reply_document(document='https://t.me/lksdjfgs/52')#2
        await message.reply_document(document='https://t.me/lksdjfgs/53')#3
        await message.reply_document(document='https://t.me/lksdjfgs/54')#4
        await message.reply_document(document='https://t.me/lksdjfgs/55')#5
        await message.reply_document(document='https://t.me/lksdjfgs/56')#6
        await message.reply_document(document='https://t.me/lksdjfgs/57')#7
        await message.reply_document(document='https://t.me/lksdjfgs/58')#8
        await message.reply_document(document='https://t.me/lksdjfgs/59')#9
        await message.reply_document(document='https://t.me/lksdjfgs/60')#10
        await message.reply_document(document='https://t.me/lksdjfgs/61')#11
        await message.reply_document(document='https://t.me/lksdjfgs/62')#12
        await message.reply_document(document='https://t.me/lksdjfgs/63')#13
        await message.reply_document(document='https://t.me/lksdjfgs/65')#14
        await message.reply_document(document='https://t.me/lksdjfgs/66')#15