import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pathlib import Path


TOKEN = "7751506046:AAG0fa7vX5_CbtnvEIYRQWOQvkwnbYgjsmI"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot, storage=MemoryStorage())

BASE_DIR = str(Path(__file__).resolve().parent)+"/src/database/database.sqlite3"
db = sqlite3.connect(BASE_DIR)
sql = db.cursor()