import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Твой секретный ключ от BotFather
API_TOKEN = '8796737204:AAEys2hDlFIe5Jp4KUIY9_QXMroUP5fAeRs'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Ответ на команду /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я твой первый бот-калькулятор. Пришли мне пример, например: 5 + 10")

# Основная логика вычислений
@dp.message()
async def calculate(message: types.Message):
    try:
        # Функция eval() выполняет строку как код (для новичка это магия)
        result = eval(message.text)
        await message.answer(f"Результат: {result}")
    except Exception:
        await message.answer("Ошибка! Пиши только цифры и знаки (+, -, *, /)")

async def main():
    print("Бот запущен и ждет сообщений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())