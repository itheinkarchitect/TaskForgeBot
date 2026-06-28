from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/task")],
        [KeyboardButton(text="/add")],
        [KeyboardButton(text="/complete")],
        [KeyboardButton(text="/delete")],
        [KeyboardButton(text="/help")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите команду"
)