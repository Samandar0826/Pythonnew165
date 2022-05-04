from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



python_m: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='3Ds max darslari'),
             KeyboardButton(text='Orqaga')
        ]

    ],
    resize_keyboard=True

)
