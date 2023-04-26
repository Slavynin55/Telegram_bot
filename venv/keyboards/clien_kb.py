from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton("/Умения")
b2 = KeyboardButton("/Кто_я")
b3 = KeyboardButton("/Меню")
#b4 = KeyboardButton("Поделиться номером", request_contact=True)
#b5 = KeyboardButton("Отправить где я", request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


kb_client.row(b1, b2,).add(b3)