from telebot import types


# Функция формирования inline разметки с кнопками для команды "/start"
async def command_start() -> object:
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_1 = types.InlineKeyboardButton('Кнопка 1')
    return markup.add(btn_1)

