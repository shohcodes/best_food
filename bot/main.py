import logging
import os
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv

from bot.api import set_photo_caption_api
import api
import texts
from bot.keyboards import main_menu_buttons, menu_button, foods_button, food_footer_button

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start_handler(message: types.Message, state: FSMContext):
    ids = await api.get_all_chat_ids_api()
    if message.from_user.id in ids:
        # await state.set_state('main_menu')
        await message.answer(texts.CHOOSE_MENU, reply_markup=await main_menu_buttons())
        await state.set_state('one_menu')
    else:
        await state.set_state('new_user')


@dp.message_handler(state='new_user')
async def name_handler(message: types.Message, state: FSMContext):
    await message.answer(texts.ENTER_NAME)
    await state.set_state('number')


@dp.message_handler(state='number')
async def number_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text
    await message.answer(texts.ENTER_NUMBER)
    await state.set_state('register')


@dp.message_handler(state='register')
async def register_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
    fullname = data['fullname']
    number = data['number']
    await start_handler(message, state)
    await api.register_api(fullname, number, message.from_user.id)
    await state.finish()


# @dp.message_handler(state='main_menu')
# async def main_menu_handler(message: types.Message, state: FSMContext):
# await message.answer(texts.CHOOSE_MENU, reply_markup=await main_menu_buttons())
# await state.set_state('one_menu')


@dp.message_handler(Text('🍽️ Menyu'), state='one_menu')
async def menu_handler(message: types.Message, state: FSMContext):
    await message.answer(texts.CHOOSE_CATEGORY, reply_markup=await menu_button())
    await state.set_state('foods')


@dp.message_handler(Text('ℹ️ Biz haqimizda'), state='one_menu')
async def about_us_handler(message: types.Message, state: FSMContext):
    await message.answer(texts.ABOUT_US_TEXT)


@dp.message_handler(Text("🛍️ Buyurtmalarim"), state='one_menu')
async def my_orders_handler(message: types.Message, state: FSMContext):
    for order in await api.my_orders_api(message.from_user.id):
        await message.answer(f"{texts.ORDER_NUMBER}: {order['id']}\n"
                             f"{texts.STATUS}: {order['status']}\n"
                             f"{texts.PAYMENT_TYPE}: {order['payment_type']}\n"
                             f"{texts.TOTAL}: {order['total_price']}")
    await state.set_state('my_orders')


@dp.callback_query_handler(state='foods')
async def foods_handler(callback: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    if await api.get_foods_of_category_api(callback.data.split('_')[1]):
        await callback.message.answer(callback.data.split('_')[0],
                                      reply_markup=await foods_button(callback.data.split('_')[1]))
        await state.update_data(current_number=1)
        await state.set_state('one_food')
    else:
        await callback.answer(texts.NO_FOODS, show_alert=True)
        await menu_handler(callback.message, state)
        await state.set_state('one_food')
    # await state.finish()


@dp.callback_query_handler(state='one_food')
async def food_detail_handler(callback: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    data = await state.get_data()
    current_number = data.get('current_number', 1)
    if callback.data == 'back':
        await menu_handler(callback.message, state)
    else:
        id = callback.data.split('_')[1]
        await bot.send_photo(callback.message.chat.id, photo=await api.get_food_photo(id),
                             reply_markup=await food_footer_button(current_number),
                             caption=await set_photo_caption_api(id))
    await state.set_state('food_footer')


@dp.callback_query_handler(lambda callback_query: callback_query.data in ['minus', 'plus', 'back'], state='food_footer')
async def handle_plus_minus_buttons(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    current_number = data.get('current_number', 1)

    if callback_query.data == 'back':
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
        await menu_handler(callback_query.message, state)

    elif callback_query.data == 'plus':
        current_number += 1
    elif callback_query.data == 'minus':
        current_number = max(1, current_number - 1)

    await state.update_data(current_number=current_number)
    updated_keyboard = await food_footer_button(current_number)

    await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=updated_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
