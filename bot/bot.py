import os
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


API_TOKEN = 'YOUR_BOT_TOKEN'
DJANGO_API_URL = 'http://web:8000/api/tasks/'
DJANGO_API_TOKEN = os.getenv("DJANGO_API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

HEADERS = {
    "Authorization": f"Token {DJANGO_API_TOKEN}",
    "Content-Type": "application/json"
}


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот для управления задачами. Используй /tasks для просмотра задач.")


@dp.message_handler(commands=['tasks'])
async def list_tasks(message: types.Message):
    response = requests.get(DJANGO_API_URL, headers=HEADERS)

    if response.status_code == 200:
        tasks = response.json()
        text = "\n".join([f"{t['title']} (Создано: {t['created_at']})" for t in tasks])
        await message.answer(text or "У вас пока нет задач.")
    else:
        await message.answer("Ошибка при получении задач.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
