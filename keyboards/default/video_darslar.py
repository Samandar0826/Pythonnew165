from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



asosiy_menu: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='Python 🐍'),
             KeyboardButton(text='3Ds Max 🏠')
        ],
        [
             KeyboardButton(text='C++ 👨‍💻'),
             KeyboardButton(text='Java script ☕')
        ],
        [
             KeyboardButton(text='Front-end 👨‍💻'),
             KeyboardButton(text='PHP ✅')
        ],
        [
             KeyboardButton(text='SMM ✅'),
             KeyboardButton(text='C# 👨‍💻')
        ],
        [
             KeyboardButton(text='Android dasturlash 📱'),
             KeyboardButton(text='Photoshop 🖼')
        ]

    ],
    resize_keyboard=True

)
