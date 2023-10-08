from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="🌐 Наш сайт", callback_data="our_website"),
    InlineKeyboardButton(text="🛄 Скачать надстройку", callback_data="download_slider")],
    [InlineKeyboardButton(text="💳 Оформить подписку", callback_data="subscribe")]
    ,
    [InlineKeyboardButton(text="ℹ️ Помощь", callback_data="get_help_menu")
     ]
]

help_menu = [
    [InlineKeyboardButton(text="🗃️ Минимальные требования", callback_data="requirements_slider")],
    [InlineKeyboardButton(text="❔ Не появилась надстройка", callback_data="disabled_slider")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
help_menu = InlineKeyboardMarkup(inline_keyboard=help_menu)

exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="📖 Главное меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])





