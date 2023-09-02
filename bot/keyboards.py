from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

import texts
from bot import api


async def main_menu_buttons():
    design = [
        [texts.MENU],
        [texts.MY_ORDERS, texts.BASKET],
        [texts.ABOUT_US]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


async def menu_button():
    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    categories = [InlineKeyboardButton(category['name'], callback_data=category['id']) for category in
                  await api.get_categories_api()]
    inline_keyboard.add(*categories)
    return inline_keyboard


async def foods_button(id):
    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    foods = (InlineKeyboardButton(food['name'], callback_data=food['id']) for food in
             await api.get_foods_of_category_api(id))
    inline_keyboard.add(*foods)
    return inline_keyboard
