import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv

import api
import texts
from bot.keyboards import main_menu_buttons, menu_button, foods_button

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start_handler(message: types.Message, state: FSMContext):
    ids = await api.get_all_chat_ids_api()
    if message.from_user.id in ids:
        await state.set_state('main_menu')
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
    await main_menu_handler(message, state)
    await api.register_api(fullname, number, message.from_user.id)
    await state.finish()


@dp.message_handler(state='main_menu')
async def main_menu_handler(message: types.Message, state: FSMContext):
    await message.answer(texts.CHOOSE_MENU, reply_markup=await main_menu_buttons())
    await state.set_state('one_menu')


@dp.message_handler(Text('🍽️ Menyu'), state='one_menu')
async def menu_handler(message: types.Message, state: FSMContext):
    await message.answer(texts.CHOOSE_CATEGORY, reply_markup=await menu_button())
    await state.set_state('foods')


@dp.message_handler(Text('ℹ️ Biz haqimizda'), state='one_menu')
async def about_us_handler(message: types.Message, state: FSMContext):
    await message.answer(texts.ABOUT_US_TEXT)
    await state.set_state('about_us_state')


@dp.message_handler(Text("🛍️ Buyurtmalarim"), state='one_menu')
async def my_orders_handler(message: types.Message, state: FSMContext):
    for order in await api.my_orders_api(message.from_user.id):
        await message.answer(f"Buturtma raqami: {order['id']}\n"
                             f"Status: {order['status']}\n"
                             f"To`lov turi: {order['payment_type']}\n"
                             f"Jami: {order['total_price']}")
    await state.set_state('my_orders')


@dp.callback_query_handler(state='foods')
async def foods_handler(callback: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    if await api.get_foods_of_category_api(callback.data):
        await callback.message.answer(texts.FOODS, reply_markup=await foods_button(callback.data))
    else:
        await callback.message.answer(texts.NO_FOODS)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
