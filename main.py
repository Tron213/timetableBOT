from aiogram import Bot, Dispatcher,executor,types
from config import API_TOKEN
from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from databaza import add_user, add_user_namb,add_user_name

bot=Bot(API_TOKEN)
dp=Dispatcher(bot, storage=MemoryStorage())

class user_reg(StatesGroup):
    name = State()
    namb= State()

dp.message_handler(state=user_reg.name)
async def add_name_(message: types.Message, state=FSMContext):
    chat_id=message.chat.id
    await state.finish()
    add_user_name(message)
    await bot.send_message(chat_id,"Отправьте номер группы")
    await user_reg.namb.set()

dp.message_handler(state=user_reg.namb)
async def add_namb(message: types.Message, state=FSMContext): 
    chat_id=message.chat.id
    await state.finish()
    add_user_namb(message)
    await bot.send_message(chat_id,"Регистрация пройдена")

@dp.message_handler(commands=["start"])
async def start_message(message: types.Message, state=FSMContext):
    chat_id =message.chat.id
    add_user(message)
    await bot.send_message(chat_id,f"Привет, {message.chat.first_name}, введи название своей кафедры:")
    await user_reg.name.set()

if __name__ =="__main__":
    executor.start_polling(dp)
