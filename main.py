from aiogram import Bot, Dispatcher,executor,types
from config import API_TOKEN
import logging
from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from databaza import IDTELE, ChangeGrp
import btns as nav
import os

from datetime import datetime, timedelta


def todayday():
    current_date = datetime.now()
    next_day = current_date + timedelta(days=0)
    formatted_date = next_day.strftime("%d.%m.%Y")
    return formatted_date
def NextDay():
    current_date = datetime.now()
    next_day = current_date + timedelta(days=1)
    formatted_date = next_day.strftime("%d.%m.%Y")
    return formatted_date
pics_folder = "C:/Users/Никита/Documents/GitHub/timetableBOT/TODAY"
pics_folder2 = "C:/Users/Никита/Documents/GitHub/timetableBOT/tomorrow"


bot=Bot(API_TOKEN)
dp=Dispatcher(bot, storage=MemoryStorage())

class sta(StatesGroup):
    Q1=State()

@dp.message_handler(commands=['start'],state=None)
async def start_command(message: types.Message):
    await message.reply("Напиши номер своей группы, например 409 или 107:")
    # Set the bot state to wait for the user's number
    await sta.Q1.set()

@dp.message_handler(state=sta.Q1)
async def grupSS(message:types.Message, state:FSMContext):
    GROUP=message.text
    IDTG=message.from_user.id
    IDTELE(IDTG,GROUP)
    sticker_id="CAACAgIAAxkBAAEJb85klGMSCbvsLWbqUnAsaZLe470mJQACCQEAAjrRBwABHCExDa0g5YsvBA"
    await message.reply_sticker(sticker=sticker_id)
    await bot.send_message(message.from_user.id,"Надеюсь всеработает)",reply_markup=nav.MainMenu)
    
    await state.finish()

@dp.message_handler()
async def navmenu(message: types.message):
    if message.text == "Сегодня⏰":
        chat_id = message.chat.id
        pics_path = os.path.join(os.getcwd(), pics_folder)
        image_files = [f for f in os.listdir(pics_path) if os.path.isfile(os.path.join(pics_path, f))]
        if not image_files:
            await message.answer("Расписание на сегодня еще не доступно")
            return
        for image_file in image_files:
            image_path = os.path.join(pics_path, image_file)
            with open(image_path, 'rb') as photo:
                await bot.send_photo(chat_id, photo)
        await message.answer("Расписание на "+ todayday())
    
    
    
    elif message.text == "Завтра 🗓️":
        chat_id = message.chat.id
        pics_path = os.path.join(os.getcwd(), pics_folder2)
        image_files = [f for f in os.listdir(pics_path) if os.path.isfile(os.path.join(pics_path, f))]
        if not image_files:
            await message.answer("Расписание на завтра еще не доступно")
            return
        for image_file in image_files:
            image_path = os.path.join(pics_path, image_file)
            with open(image_path, 'rb') as photo:
                await bot.send_photo(chat_id, photo)
        await message.answer("Расписание на "+ NextDay())
    


    elif message.text=="Поменять группу✏️":
        await bot.send_message(message.from_user.id,"ваша группа удалена, перезапутсите бота с помощью команда /start")
        IDTG=message.from_user.id
        ChangeGrp(IDTG)


if __name__ =="__main__":
    executor.start_polling(dp,skip_updates=True)
