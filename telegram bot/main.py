import logging
from typing import Text
from aiogram import Bot, Dispatcher, executor, types
from sys import exit
import json

from aiogram.types import message
import config, question



#забираем токен из конфига

bot = (config.token) #забираем токен
songs = (question.songs) #импортируем json
dictData = json.loads(songs)

text_answer = (dictData["answer"]) #Вытаскиваем ответ
text_question = (dictData["question"]) #Вытаскиваем вопрос

bot_token = bot
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)


# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


# Хэндлер на команду /test2
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")

dp.register_message_handler(cmd_test2, commands="test2")





@dp.message_handler(commands="dice")
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")





#Хэндлер на команду /question



#dictData = json.loads(songs)
#text_question = (dictData["question"])

@dp.message_handler(commands="question")


async def cmd_question(message: types.Message):
    await message.reply(text_question)







##################################################

# получение ответа на вопрос





#@dp.message_handler(commands="Героиня")

@dp.message_handler()

async def answer_message(msg: types.Message):
    client_text = (msg["text"])
    if text_answer == client_text:
        await bot.send_message(msg.from_user.id, 'Правильно')
        print(msg)
    else:
        await bot.send_message(msg.from_user.id, 'Не правильно')
        print(msg)
    # print(client_text)



##################################################
from aiogram.utils.exceptions import BotBlocked





@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True




if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)