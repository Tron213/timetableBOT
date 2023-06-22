from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ToDayBtn=KeyboardButton("Сегодня⏰")
ToMorowBtn=KeyboardButton("Завтра 🗓️")
DellGroup=KeyboardButton("Поменять группу✏️")
MainMenu=ReplyKeyboardMarkup(resize_keyboard=True).add(ToDayBtn,ToMorowBtn,DellGroup)