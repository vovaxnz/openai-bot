from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from simple_inference import simple_inference_fine_tuned
from translation import translate_text


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def _preprocess_message(text):
    translated_text = translate_text(text, language_to=['en'])
    return f'The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. \n\nPerson: {translated_text}\nAI:'


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет. Можем пообщаться на любые интересующие вас темы")

@dp.message_handler()
async def echo_message(msg: types.Message):
    preprocessed_input = _preprocess_message(msg.text)
    response_eng = simple_inference_fine_tuned(preprocessed_input)
    response_ru = translate_text(response_eng, language_to=['ru'])
    await bot.send_message(msg.from_user.id, response_ru)


if __name__ == '__main__':
    executor.start_polling(dp)
