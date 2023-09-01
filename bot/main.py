import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from bot.handlers import *
load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    logging.basicConfig(level=logging.INFO)


