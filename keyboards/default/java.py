from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



python_j: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='Java script darslari'),
             KeyboardButton(text='Orqaga')
        ]

    ],
    resize_keyboard=True

)
