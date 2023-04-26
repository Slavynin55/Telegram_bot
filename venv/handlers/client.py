from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite


#@dp.message_handler(commands=["start", "help"])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, "Добро пожаловать", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Бот не может Вам написать первым в ЛС, поэтому напишите ему сами: \nhttps://t.me/Vasya_pyshistiy_bot")

#@dp.message_handler(commands=["Что_я_умею"])
async def opport_command(message : types.Message):
    await bot.send_message(message.from_user.id, "Пока я очень маленький и слабенький бот, умею отвечать только на команды, но со временем я стану настоящим Автоботом :)")


#@dp.message_handler(commands=["Кто_я"])
async def name_command(message : types.Message):
    await bot.send_message(message.from_user.id, "Меня зовут Вася и я бот,  я пока работаю только когда включен компьютер(")
#@dp.message_handler(commands=["Меню"])
async def menu_command(message : types.Message):
    await sqlite.sql_read(message)



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', "help"])
    dp.register_message_handler(opport_command, commands=["Умения"])
    dp.register_message_handler(name_command, commands=["Кто_я"])
    dp.register_message_handler(menu_command, commands=["Меню"])