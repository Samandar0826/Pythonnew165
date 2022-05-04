from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



python_a: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='Android dasturlash darslari'),
             KeyboardButton(text='Orqaga')
        ]

    ],
    resize_keyboard=True

)