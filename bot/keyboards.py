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
    categories = [InlineKeyboardButton(category['name'], callback_data=f"{category['name']}_{category['id']}") for
                  category in
                  await api.get_categories_api()]
    inline_keyboard.add(*categories)
    return inline_keyboard


async def foods_button(id):
    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    foods = (InlineKeyboardButton(food['name'], callback_data=f"{food['name']}_{food['id']}") for food in
             await api.get_foods_of_category_api(id))
    inline_keyboard.add(*foods)
    inline_keyboard.add(InlineKeyboardButton('⬅ Ortga', callback_data='back'))
    return inline_keyboard


async def back_button():
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    inline_keyboard.add(InlineKeyboardButton('⬅ Ortga', callback_data='back'))
    return inline_keyboard


async def food_footer_button(current_number):
    inline_keyboard = InlineKeyboardMarkup()
    inline_keyboard.add(InlineKeyboardButton('➖', callback_data='minus'),
                        InlineKeyboardButton(str(current_number), callback_data='number'),
                        InlineKeyboardButton('➕', callback_data='plus'),
                        InlineKeyboardButton(texts.ADD_TO_BASKET, callback_data='add_to_basket'))
    inline_keyboard.add(InlineKeyboardButton('⬅ Ortga', callback_data='back'))
    return inline_keyboard


async def basket_button():
    inline_button = InlineKeyboardMarkup(row_width=2)
    inline_button.add(InlineKeyboardButton(texts.EMPTY_BASKET, callback_data='empty_basket'),
                      InlineKeyboardButton(texts.CONFIRM, callback_data='confirm'))
    return inline_button
