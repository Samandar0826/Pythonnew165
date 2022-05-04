from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



python_c: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='C++ darslari'),
             KeyboardButton(text='Orqaga')
        ]

    ],
    resize_keyboard=True

)