from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



python_s: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='SMM darslari'),
             KeyboardButton(text='Orqaga')
        ]

    ],
    resize_keyboard=True

)