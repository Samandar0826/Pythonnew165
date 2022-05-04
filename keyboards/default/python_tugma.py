from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



python_s: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='Python darslari'),
             KeyboardButton(text='Orqaga')
        ]

    ],
    resize_keyboard=True

)
