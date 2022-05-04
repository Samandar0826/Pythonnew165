from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



python_f: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='Front-end darslari'),
             KeyboardButton(text='Orqaga')
        ]

    ],
    resize_keyboard=True

)
