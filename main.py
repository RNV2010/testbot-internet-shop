import asyncio

from telebot.async_telebot import AsyncTeleBot

import keys
import texts
import buttons

# Инициализация объекта бота
bot = AsyncTeleBot(keys.tgtoken, parse_mode='HTML')


# Перехватчик '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message) -> None:
    if message.text == '/start':
        await bot.send_message(message.chat.id, texts.command_start, reply_markup=buttons.command_start())
    elif message.text == '/help':
        await bot.send_message(message.chat.id, texts.command_help)


# Перехват всех сообщений типа 'text' (content_types по умолчанию ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message) -> None:
    await bot.reply_to(message, texts.user_text.format(message.text))





asyncio.run(bot.polling())