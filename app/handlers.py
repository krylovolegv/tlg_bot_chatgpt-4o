from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Вас приветствует MVSTER_bot!')

@router.message()
async def handle_message(message: Message):
    # Add your logic here to handle incoming messages
    await message.answer(f'Доброго времени суток Вам желает MVSTER_bot!')


