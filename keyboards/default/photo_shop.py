from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



python_ph: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='Photoshop darslari'),
             KeyboardButton(text='Orqaga')
        ]

    ],
    resize_keyboard=True

)
