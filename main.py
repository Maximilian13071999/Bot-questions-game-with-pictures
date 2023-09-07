import random

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="5644768745:AAGOrfSr-ZI62Dylu6PXVgp4IBXBDFEf70U")
dp = Dispatcher(bot)

exp = 0
level = 1

questions = [["1.png", "2.png", "3.png", "4.png"]]
answers = [3]

actual_quest = 0

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет, напиши /вопрос, чтобы начать игру")

@dp.message_handler(commands=["вопрос"])
async def get_quest(message: types.Message):
    global actual_quest
    actual_quest = random.randint(0, len(questions) - 1)
    await message.answer("Выберите лишнюю картинку")
    for photo in questions[actual_quest]:
        await bot.send_photo(message.chat.id, photo=types.InputFile(path_or_bytesio=photo))

@dp.message_handler()
async def get_answer(message: types.Message):
    if message.text.lower() == str(answers[actual_quest]):
        await message.answer("Правильно")
    else:
        await message.answer("Неправильно")

executor.start_polling(dp, skip_updates=True)